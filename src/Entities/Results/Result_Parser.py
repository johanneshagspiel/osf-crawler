import json
from datetime import datetime

from src.Entities.Registration_Supplements.Registration_Supplement_Factory import Registration_Supplement_Factory
from src.Entities.Registration_Supplements.Versions.Empty_Registration_Supplement import Empty_Registration_Supplement
from src.Entities.Results.Search_Result_API.Preprint_Result import Preprint_Result
from src.Entities.Results.Search_Result_API.Search_Result_API import Search_Result_API
from src.Entities.Util.Helper import SafeDatetimeConverter


class Result_Parser:

    @staticmethod
    def parse_registrations(data, page_number):

        new_result_list = []

        for entry in data:

            _id = entry["id"]

            title = entry["attributes"]["title"]
            description = entry["attributes"]["description"]

            date_created = SafeDatetimeConverter.string_to_datetime(entry["attributes"]["date_created"])
            date_registered = SafeDatetimeConverter.string_to_datetime(entry["attributes"]["date_registered"])

            tag_list = entry["attributes"]["tags"]
            subject_list = [item["text"] for sublist in entry["attributes"]["subjects"] for item in sublist]

            registration_form = entry["attributes"]["registration_supplement"]
            registration_supplement = Registration_Supplement_Factory.create_registration_supplement(registration_form, entry["attributes"]["registration_responses"], entry)

            if isinstance(registration_supplement, Empty_Registration_Supplement):
                registration_form = "Empty Registration Form"

            if "region" in entry["relationships"]:
                region = entry["relationships"]["region"]["links"]["related"]["href"].split("/")[5]
            else:
                region = None

            new_search_result_api = Search_Result_API(_id, title, description, date_created, date_registered,
                                                      tag_list, subject_list, registration_form, registration_supplement, region)

            new_result_list.append(new_search_result_api)

        last_search_result = new_result_list[-1]
        last_search_entry = {
            "last_page": page_number,
            "last_id": last_search_result._id,
            "timestamp_modified": datetime.now()
        }

        return new_result_list, last_search_entry


    @staticmethod
    def parse_preprints(data, page_number):
        new_result_list = []

        for entry in data:
            _id = entry["id"]

            title = entry["attributes"]["title"]
            description = entry["attributes"]["description"]

            date_created = SafeDatetimeConverter.string_to_datetime(entry["attributes"]["date_created"])
            date_published = SafeDatetimeConverter.string_to_datetime(entry["attributes"]["date_published"])

            tag_list = entry["attributes"]["tags"]
            subject_list = [item["text"] for sublist in entry["attributes"]["subjects"] for item in sublist]

            new_preprint_object = Preprint_Result(_id, title, description, date_created, date_published,
                 tag_list, subject_list)
            new_result_list.append(new_preprint_object)

        last_search_result = new_result_list[-1]
        last_search_entry = {
            "last_page": page_number,
            "last_id": last_search_result._id,
            "timestamp_modified": datetime.now()
        }

        return new_result_list, last_search_entry
