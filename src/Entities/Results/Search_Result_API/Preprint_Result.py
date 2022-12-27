
class Preprint_Result:

    def __init__(self, _id, title, description, date_created, date_published,
                 tag_list, subject_list):

        self._id = _id
        self.title = title
        self.description = description

        # Dates
        self.date_created = date_created
        self.date_published = date_published

        # Identification
        self.tag_list = tag_list
        self.subject_list = subject_list

    def to_object(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,

            "date_created": self.date_created,
            "date_published": self.date_published,

            "tag_list": self.tag_list,
            "subject_list": self.subject_list,
        }
