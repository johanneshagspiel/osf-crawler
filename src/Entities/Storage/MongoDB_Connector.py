import pymongo
from pymongo import MongoClient
from src.Entities.Storage.MongoDB_Credentials import MongoDB_Credentials


class MongoDB_Connector:

    def __init__(self):
        client = MongoClient(MongoDB_Credentials.CONNECTION_STRING)
        self.db = client[MongoDB_Credentials.COLLECTION_NAME]



    def add_entries(self, mode, entry_list):
        collection_name = mode
        original_collection = self.db[collection_name]
        collection_duplicates_name = collection_name + "_duplicates"
        duplicate_collection = self.db[collection_duplicates_name]

        for entry in entry_list:
            try:
                original_collection.insert_one(entry)
            except pymongo.errors.DuplicateKeyError:
                prev_id = entry["_id"]
                entry["osf_id"] = prev_id
                entry.pop("_id")
                duplicate_collection.insert_one(entry)
                print(f"Duplicate with id {prev_id} encountered")
                print("---")

    def id_exists(self, mode, check_id):
        collection_name = mode
        collection = self.db[collection_name]
        return collection.count_documents(filter={"_id": check_id}) > 0


    def get_first_id(self, mode):
        collection_name = mode + "_log"
        collection = self.db[collection_name]

        first_id_exists = collection.count_documents({"first_id":{"$exists":True}}) > 0

        if first_id_exists:
            return collection.find_one(filter={"first_id":{"$exists":True}})
        else:
            return None

    def create_first_id(self, mode, first_entry):
        collection_name = mode + "_log"
        collection = self.db[collection_name]
        collection.insert_one(first_entry)

    def update_first_id(self, mode, first_entry):
        collection_name = mode + "_log"
        collection = self.db[collection_name]
        new_val = {"$set": first_entry}
        collection.update_one({"_id": "first_id_log"}, new_val)


    def get_last_entry(self, mode):
        collection_name = mode + "_log"
        collection = self.db[collection_name]
        return collection.find_one(filter={"_id": "last_entry_log"})

    def create_last_entry(self, mode, last_entry):
        collection_name = mode + "_log"
        collection = self.db[collection_name]
        collection.insert_one(last_entry)

    def update_last_entry(self, mode, last_entry):
        collection_name = mode + "_log"
        collection = self.db[collection_name]
        new_val = {"$set": last_entry}
        collection.update_one({"_id":"last_entry_log"}, new_val)


    def get_all_documents(self, mode):
        collection_name = mode
        collection = self.db[collection_name]
        result_list = []

        for entry in collection.find():
            result_list.append(entry)
        return result_list

    def get_filtered_documents(self, mode, filter_type):
        collection_name = mode
        collection = self.db[collection_name]
        result_list = []

        if filter_type == "psychology_subject":
            filter = { "subject_list" : { "$elemMatch" : { "$regex" : "Psychology", "$options" : "i" } } }

        elif filter_type == "psychotherapy":
            filter = { "$or" : [
                                     {"subject_list" : { "$elemMatch" : { "$regex" : "psychotherapy", "$options" : "i" } } },
                                     {"tag_list" : { "$elemMatch" : { "$regex" : "psychotherapy", "$options" : "i" } }},
                                     {"title": {"$regex": "psychotherapie | psychotherapy", "$options": "i"}},
                                     {"description": {"$regex": "psychotherapie | psychotherapy", "$options": "i"}}
                                 ]
                       }

        for entry in collection.find(filter=filter):
            result_list.append(entry)
        return result_list


    def duplicate_collection(self, mode):
        collection_name = mode
        source_collection = self.db[collection_name]
        collection_name_duplicate = collection_name + "_clone"
        target_collection = self.db[collection_name_duplicate]

        for a in source_collection.find():
            target_collection.insert_one(a)
