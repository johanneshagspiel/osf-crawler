import json
from datetime import datetime
from random import uniform
from time import sleep
import requests
from src.Entities.Results.Result_Parser import Result_Parser
from src.Entities.Storage.MongoDB_Connector import MongoDB_Connector


class OSF_API:

    def __init__(self):
        self.storage = MongoDB_Connector()


    def get_all_projects(self, mode):

        print(f"Getting all {mode} from osf.io")

        first_id = self.storage.get_first_id(mode)

        if not first_id:
            self.download_first_time(mode)
        else:
            self.restart_download(mode)


    def download_first_time(self, mode):

        max_page_number = int(self.get_max_page_number(mode))

        url = f"https://api.osf.io/v2/{mode}/"

        print(f"Downloading page 1/{max_page_number}")

        first_url = url + "?page=1"
        first_result_list, first_last_search_entry = self.download_url(mode, first_url, 1)
        first_store_list = [x.to_object() for x in first_result_list]

        self.storage.add_entries(mode, first_store_list)

        first_entry = {}
        first_entry["_id"] = "first_id_log"
        first_entry["first_id"] = first_result_list[0]._id
        first_entry["timestamp_modified"] = datetime.now()

        self.storage.create_first_id(mode, first_entry)
        first_last_search_entry["_id"] = "last_entry_log"
        self.storage.create_last_entry(mode, first_last_search_entry)

        print(f"Finished downloading page 1/{max_page_number}")

        random_wait_time = uniform(1.0, 5.0)
        sleep(random_wait_time)

        self.download_pages(mode=mode, start_page=2)


    def restart_download(self, mode):

        first_id_dic = self.storage.get_first_id(mode)
        self.catch_up_to_first_id(mode=mode, previous_first_id_dic=first_id_dic)

        last_entry_dic = self.storage.get_last_entry(mode)
        restart_page = self.catch_up_to_last_entry(mode, last_entry_dic)

        self.download_pages(mode=mode, start_page=restart_page)


    def download_pages(self, mode, start_page):

        max_page_number = int(self.get_max_page_number(mode=mode))
        url = f"https://api.osf.io/v2/{mode}/"

        for page_number in range(start_page, max_page_number + 1):

            percentage = format(page_number / max_page_number, '.4f')
            print(f"Downloading \t\t\tpage: {page_number}/{max_page_number} - {percentage}%")

            next_url = url + f"?page={page_number}"
            result_list, last_search_entry = self.download_url(mode=mode, url=next_url, page_number=page_number)
            store_list = [x.to_object() for x in result_list]

            self.storage.add_entries(mode=mode, entry_list=store_list)
            self.storage.update_last_entry(mode=mode, last_entry=last_search_entry)

            print(f"Finished downloading \tpage: {page_number}/{max_page_number} - {percentage}%")

            random_wait_time = uniform(1.0, 5.0)
            sleep(random_wait_time)

    def catch_up_to_last_entry(self, mode, last_entry_dic):
        url = f"https://api.osf.io/v2/{mode}/"
        page_number = last_entry_dic["last_page"]

        not_caught_up = True
        last_search_entry = None

        while not_caught_up:
            print(f"Downloading page {page_number} of {mode} to catch up to the last previously downloaded id")

            next_url = url + f"?page={page_number}"
            result_list, last_search_entry = self.download_url(mode, next_url, page_number)

            check_list = [(x._id, x.to_object()) for x in result_list]

            store_list = []
            for id, store_object in check_list:

                if id == last_entry_dic["last_id"]:
                    not_caught_up = False

                if not self.storage.id_exists(mode, id):
                    store_list.append(store_object)

            if len(store_list) > 0:
                self.storage.add_entries(mode, store_list)

            print(f"Finished downloading page {page_number} of {mode} to catch up to the last previously downloaded id")

            page_number += 1
            random_wait_time = uniform(1.0, 5.0)
            sleep(random_wait_time)

        self.storage.update_last_entry(mode, last_search_entry)
        print(f"Found last previously downloaded id of {mode} on page {page_number - 1}")
        print(" ")
        return page_number

    def catch_up_to_first_id(self, mode, previous_first_id_dic):
        url = f"https://api.osf.io/v2/{mode}/"
        page_number = 1

        not_caught_up = True
        first_time = True
        new_first_id = None

        while not_caught_up:
            print(f"Downloading {mode} page {page_number} to catch up to the first previously downloaded id")

            next_url = url + f"?page={page_number}"
            result_list, last_search_entry = self.download_url(mode=mode, url=next_url, page_number=page_number)

            check_list = [(x._id, x.to_object()) for x in result_list]

            if first_time:
                new_first_id = check_list[0][0]
                first_time = False

            store_list = []
            for id, store_object in check_list:

                if id == previous_first_id_dic["first_id"]:
                    not_caught_up = False

                if not self.storage.id_exists(mode, id):
                    store_list.append(store_object)

            if len(store_list) > 0:
                self.storage.add_entries(mode, store_list)

            print(f"Finished downloading {mode} page {page_number} to catch up to the first previously downloaded id")

            page_number += 1
            random_wait_time = uniform(1.0, 5.0)
            sleep(random_wait_time)

        page_number -= 1
        first_entry = {}
        first_entry["_id"] = "first_id_log"
        first_entry["first_id"] = new_first_id
        first_entry["timestamp_modified"] = datetime.now()
        self.storage.update_first_id(mode, first_entry)
        print(f"Found first previously downloaded id of {mode} on page {page_number}")
        print(" ")


    def get_max_page_number(self, mode):
        url = f"https://api.osf.io/v2/{mode}/"
        personal_access_token = "3JtLxDvhH4u0h9j61OFY3RaKGi9tfwTYB3T7MymwCHxiSichc1j3B6qCMYGSdf5I0uEsYu"
        authorization_value_str = f"Bearer {personal_access_token}"
        headers = {'Authorization': authorization_value_str}

        keep_downloading = True

        while keep_downloading:
            try:
                response = requests.get(url, headers=headers)
                result = response.text
                keep_downloading = False

            except Exception as e:
                print(e)
                random_wait_time = uniform(1.0, 5.0)
                sleep(random_wait_time)

        return json.loads(result)["links"]["last"].split("page=")[1]


    def download_url(self, mode, url, page_number):

        personal_access_token = "3JtLxDvhH4u0h9j61OFY3RaKGi9tfwTYB3T7MymwCHxiSichc1j3B6qCMYGSdf5I0uEsYu"
        authorization_value_str = f"Bearer {personal_access_token}"
        headers = {'Authorization': authorization_value_str}

        keep_downloading = True

        while keep_downloading:
            try:
                response = requests.get(url, headers=headers)
                result = response.text
                keep_downloading = False

            except Exception as e:
                print(e)
                random_wait_time = uniform(1.0, 5.0)
                sleep(random_wait_time)

        data = json.loads(result)["data"]

        if mode == "registrations":
            return Result_Parser.parse_registrations(data, page_number)

        elif mode == "preprints":
            return Result_Parser.parse_preprints(data, page_number)

