
class Secondary_Data_Preregistration():

    def __init__(self, research_question, hypotheses, dataset, dataset_availability, data_access, data_identifiers,
                 access_date, data_collection_procedure, codebook, manipulated_variables, measured_variables,
                 units_of_analysis, missing_data, statistical_outlier, sampling_weights, work_references,
                 prior_knowledge, statistical_model, effect_size, statistical_power, inference_criteria, data_problems,
                 hypothesis_test, exploratory_analysis):

        self.research_question = research_question
        self.hypotheses = hypotheses
        self.dataset = dataset
        self.dataset_availability = dataset_availability
        self.data_access = data_access
        self.data_identifiers = data_identifiers
        self.access_date = access_date
        self.data_collection_procedure = data_collection_procedure
        self.codebook = codebook
        self.manipulated_variables = manipulated_variables
        self.measured_variables = measured_variables
        self.units_of_analysis = units_of_analysis
        self.missing_data = missing_data
        self.statistical_outlier = statistical_outlier
        self.sampling_weights = sampling_weights
        self.work_references = work_references
        self.prior_knowledge = prior_knowledge
        self.statistical_model = statistical_model
        self.effect_size = effect_size
        self.statistical_power = statistical_power
        self.inference_criteria = inference_criteria
        self.data_problems = data_problems
        self.hypothesis_test = hypothesis_test
        self.exploratory_analysis = exploratory_analysis

    def to_object(self):
        return {
           "research_question": self.research_question,
           "hypotheses": self.hypotheses,
            "dataset": self.dataset,
            "dataset_availability": self.dataset_availability,
            "data_access": self.data_access,
            "data_identifiers": self.data_identifiers,
            "access_date": self.access_date,
            "data_collection_procedure": self.data_collection_procedure,
            "codebook": self.codebook,
            "manipulated_variables": self.manipulated_variables,
            "measured_variables": self.measured_variables,
            "units_of_analysis": self.units_of_analysis,
            "missing_data": self.missing_data,
            "statistical_outlier": self.statistical_outlier,
            "sampling_weights": self.sampling_weights,
            "work_references": self.work_references,
            "prior_knowledge": self.prior_knowledge,
            "statistical_model": self.statistical_model,
            "effect_size": self.effect_size,
            "statistical_power": self.statistical_power,
            "inference_criteria": self.inference_criteria,
            "data_problems": self.data_problems,
            "hypothesis_test": self.hypothesis_test,
            "exploratory_analysis": self.exploratory_analysis
        }