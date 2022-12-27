
class AsPredicted_Preregistration:

    def __init__(self, data, hypothesis, dependent, conditions, analyses, outliers, sample, other, name, study_type,
                 study_type_other):

        self.data = data
        self.hypothesis = hypothesis
        self.dependent = dependent
        self.conditions = conditions
        self.analyses = analyses
        self.outliers = outliers
        self.sample = sample
        self.other = other
        self.name = name
        self.study_type = study_type
        self.study_type_other = study_type_other

    def to_object(self):
        return {
            "data": self.data,
            "hypothesis": self.hypothesis,
            "dependent": self.dependent,
            "conditions": self.conditions,
            "analyses": self.analyses,
            "outliers": self.outliers,
            "sample": self.sample,
            "other": self.other,
            "name": self.name,
            "study_type": self.study_type,
            "study_type_other": self.study_type_other
        }