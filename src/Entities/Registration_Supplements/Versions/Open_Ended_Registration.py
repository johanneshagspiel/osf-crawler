
class Open_Ended_Registration():

    def __init__(self, summary):
        self.summary = summary

    def to_object(self):
        return {
            "summary": self.summary
        }