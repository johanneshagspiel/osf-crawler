
class OSF_Preregistration:

    def __init__(self, hypotheses, study_type, blinding, additional_blinding_information, study_design, randomization,
                 existing_data, explanation_existing_data, data_collection_procedures, sample_size, sample_size_rational,
                 stopping_rule, manipulated_variables, measured_variables, indices, statistical_models, transformations,
                 inference_criteria, data_exclusion, missing_data, exploratory_analysis, other):

        self.hypotheses = hypotheses
        self.study_type = study_type
        self.blinding = blinding
        self.additional_blinding_information = additional_blinding_information
        self.study_design = study_design
        self.randomization = randomization
        self.existing_data = existing_data
        self.explanation_existing_data = explanation_existing_data
        self.data_collection_procedures = data_collection_procedures
        self.sample_size = sample_size
        self.sample_size_rational = sample_size_rational
        self.stopping_rule = stopping_rule
        self.manipulated_variables = manipulated_variables
        self.measured_variables = measured_variables
        self.indices = indices
        self.statistical_models = statistical_models
        self.transformations = transformations
        self.inference_criteria = inference_criteria
        self.data_exclusion = data_exclusion
        self.missing_data = missing_data
        self.exploratory_analysis = exploratory_analysis
        self.other = other

    def to_object(self):
        return {
            "hypotheses": self.hypotheses,
            "study_type": self.study_type,
            "blinding": self.blinding,
            "additional_blinding_information": self.additional_blinding_information,
            "study_design": self.study_design,
            "randomization": self.randomization,
            "existing_data": self.existing_data,
            "explanation_existing_data": self.explanation_existing_data,
            "data_collection_procedures": self.data_collection_procedures,
            "sample_size": self.sample_size,
            "sample_size_rational": self.sample_size_rational,
            "stopping_rule": self.stopping_rule,
            "manipulated_variables": self.manipulated_variables,
            "measured_variables": self.measured_variables,
            "indices": self.indices,
            "statistical_models": self.statistical_models,
            "transformations": self.transformations,
            "inference_criteria": self.inference_criteria,
            "data_exclusion": self.data_exclusion,
            "missing_data": self.missing_data,
            "exploratory_analysis": self.exploratory_analysis,
            "other": self.other
        }