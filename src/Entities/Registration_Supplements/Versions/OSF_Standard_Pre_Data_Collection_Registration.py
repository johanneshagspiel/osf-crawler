

class OSF_Standard_Pre_Data_Collection_Registration:

    def __init__(self, datacompletion, looked, comments):

        self.datacompletion = datacompletion
        self.looked = looked
        self.comments = comments

    def to_object(self):
        return {
            "datacompletion": self.datacompletion,
            "looked": self.looked,
            "comments": self.comments
        }