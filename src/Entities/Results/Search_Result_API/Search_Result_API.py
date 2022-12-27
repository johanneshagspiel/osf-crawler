
class Search_Result_API:

    def __init__(self, _id, title, description, date_created, date_registered,
                 tag_list, subject_list,
                 registration_form, registration_supplement,
                 region):

        self._id = _id
        self.title = title
        self.description = description

        #Dates
        self.date_created = date_created
        self.date_registered = date_registered

        #Identification
        self.tag_list = tag_list
        self.subject_list = subject_list

        #Research Supplement
        self.registration_form = registration_form
        self.registration_supplement = registration_supplement

        #Other
        self.region = region

    def to_object(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,

            "date_created": self.date_created,
            "date_registered": self.date_registered,

            "tag_list": self.tag_list,
            "subject_list": self.subject_list,

            "registration_form": self.registration_form,
            "registration_supplement": self.registration_supplement.to_object(),

            "region": self.region,
        }
