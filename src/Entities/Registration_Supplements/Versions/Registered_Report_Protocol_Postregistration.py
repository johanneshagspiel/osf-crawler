
class Registered_Report_Protocol_Postregistration:

    def __init__(self, final_design, effect_size, confidence_interval, replication_effect_size, replication_judgment,
                 replication_judgment_reason, data, analyses, limitations):

        self.final_design = final_design
        self.effect_size = effect_size
        self.confidence_interval = confidence_interval
        self.replication_effect_size = replication_effect_size
        self.replication_judgment = replication_judgment
        self.replication_judgment_reason = replication_judgment_reason
        self.data = data
        self.analyses = analyses
        self.limitations = limitations

    def to_object(self):
        return {
            "final_design": self.final_design,
            "effect_size": self.effect_size,
            "confidence_interval": self.confidence_interval,
            "replication_effect_size": self.replication_effect_size,
            "replication_judgment": self.replication_judgment,
            "replication_judgment_reason": self.replication_judgment_reason,
            "data": self.data,
            "analyses": self.analyses,
            "limitations": self.limitations
        }