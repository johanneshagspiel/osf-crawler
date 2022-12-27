
class Registered_Report_Protocol_Preregistration:

    def __init__(self, in_principle_acceptance, journal_title, date_in_principle_acceptance, other):

        self.in_principle_acceptance = in_principle_acceptance
        self.journal_title = journal_title
        self.date_in_principle_acceptance = date_in_principle_acceptance
        self.other = other

    def to_object(self):
        return {
            "in_principle_acceptance": self.in_principle_acceptance,
            "journal_title": self.journal_title,
            "date_in_principle_acceptance": self.date_in_principle_acceptance,
            "other": self.other
        }