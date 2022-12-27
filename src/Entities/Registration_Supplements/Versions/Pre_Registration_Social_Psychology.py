
class Pre_Registration_Social_Psychology:

    def __init__(self, description_hypothesis_question1a,
        description_hypothesis_question2a,
        description_hypothesis_question3a,
        description_hypothesis_question4a,
        recommended_hypothesis_question5a,
        recommended_hypothesis_question6a,
        description_methods_design_question2a,
        description_methods_design_question2b,
        description_methods_design_question3b,
        description_methods_planned_sample_question4b,
        description_methods_planned_sample_question5b,
        description_methods_planned_sample_question6b,
        description_methods_planned_sample_question6b_upload,
        description_methods_planned_sample_question7b,
        description_methods_exclusion_criteria_question8b,
        description_methods_procedure_question10b,
        recommended_methods_procedure_question9b,
        recommended_methods_procedure_question9b_file,
        confirmatory_analyses_first_first_question1c,
        confirmatory_analyses_first_first_question2c,
        confirmatory_analyses_first_first_question3c,
        confirmatory_analyses_first_first_question4c,
        confirmatory_analyses_first_first_question5c,
        confirmatory_analyses_second_second_question1c,
        confirmatory_analyses_second_second_question2c,
        confirmatory_analyses_second_second_question3c,
        confirmatory_analyses_second_second_question4c,
        confirmatory_analyses_second_second_question5c,
        confirmatory_analyses_third_third_question1c,
        confirmatory_analyses_third_third_question2c,
        confirmatory_analyses_third_third_question3c,
        confirmatory_analyses_third_third_question4c,
        confirmatory_analyses_third_third_question5c,
        confirmatory_analyses_fourth_fourth_question1c,
        confirmatory_analyses_fourth_fourth_question2c,
        confirmatory_analyses_fourth_fourth_question3c,
        confirmatory_analyses_fourth_fourth_question4c,
        confirmatory_analyses_fourth_fourth_question5c,
        confirmatory_analyses_further_further_question1c,
        confirmatory_analyses_further_further_question2c,
        confirmatory_analyses_further_further_question3c,
        confirmatory_analyses_further_further_question4c,
        confirmatory_analyses_further_further_question5c,
        recommended_analysis_specify_question6c,
        recommended_analysis_specify_question7c,
        recommended_analysis_specify_question8c,
        recommended_analysis_specify_question9c,
        recommended_analysis_specify_question10c,
        recommended_analysis_specify_question11c,
        datacompletion,
        looked,
        dataCollectionDates,
        additionalComments,
        ):
        
        self.description_hypothesis_question1a = description_hypothesis_question1a
        self.description_hypothesis_question2a = description_hypothesis_question2a
        self.description_hypothesis_question3a = description_hypothesis_question3a
        self.description_hypothesis_question4a = description_hypothesis_question4a
        self.recommended_hypothesis_question5a = recommended_hypothesis_question5a
        self.recommended_hypothesis_question6a = recommended_hypothesis_question6a
        self.description_methods_design_question2a = description_methods_design_question2a
        self.description_methods_design_question2b = description_methods_design_question2b
        self.description_methods_design_question3b = description_methods_design_question3b
        self.description_methods_planned_sample_question4b = description_methods_planned_sample_question4b
        self.description_methods_planned_sample_question5b = description_methods_planned_sample_question5b
        self.description_methods_planned_sample_question6b = description_methods_planned_sample_question6b
        self.description_methods_planned_sample_question6b_upload = description_methods_planned_sample_question6b_upload
        self.description_methods_planned_sample_question7b = description_methods_planned_sample_question7b
        self.description_methods_exclusion_criteria_question8b = description_methods_exclusion_criteria_question8b
        self.description_methods_procedure_question10b = description_methods_procedure_question10b
        self.recommended_methods_procedure_question9b = recommended_methods_procedure_question9b
        self.recommended_methods_procedure_question9b_file = recommended_methods_procedure_question9b_file
        self.confirmatory_analyses_first_first_question1c = confirmatory_analyses_first_first_question1c
        self.confirmatory_analyses_first_first_question2c = confirmatory_analyses_first_first_question2c
        self.confirmatory_analyses_first_first_question3c = confirmatory_analyses_first_first_question3c
        self.confirmatory_analyses_first_first_question4c = confirmatory_analyses_first_first_question4c
        self.confirmatory_analyses_first_first_question5c = confirmatory_analyses_first_first_question5c
        self.confirmatory_analyses_second_second_question1c = confirmatory_analyses_second_second_question1c
        self.confirmatory_analyses_second_second_question2c = confirmatory_analyses_second_second_question2c
        self.confirmatory_analyses_second_second_question3c = confirmatory_analyses_second_second_question3c
        self.confirmatory_analyses_second_second_question4c = confirmatory_analyses_second_second_question4c
        self.confirmatory_analyses_second_second_question5c = confirmatory_analyses_second_second_question5c
        self.confirmatory_analyses_third_third_question1c = confirmatory_analyses_third_third_question1c
        self.confirmatory_analyses_third_third_question2c = confirmatory_analyses_third_third_question2c
        self.confirmatory_analyses_third_third_question3c = confirmatory_analyses_third_third_question3c
        self.confirmatory_analyses_third_third_question4c = confirmatory_analyses_third_third_question4c
        self.confirmatory_analyses_third_third_question5c = confirmatory_analyses_third_third_question5c
        self.confirmatory_analyses_fourth_fourth_question1c = confirmatory_analyses_fourth_fourth_question1c
        self.confirmatory_analyses_fourth_fourth_question2c = confirmatory_analyses_fourth_fourth_question2c
        self.confirmatory_analyses_fourth_fourth_question3c = confirmatory_analyses_fourth_fourth_question3c
        self.confirmatory_analyses_fourth_fourth_question4c = confirmatory_analyses_fourth_fourth_question4c
        self.confirmatory_analyses_fourth_fourth_question5c = confirmatory_analyses_fourth_fourth_question5c
        self.confirmatory_analyses_further_further_question1c = confirmatory_analyses_further_further_question1c
        self.confirmatory_analyses_further_further_question2c = confirmatory_analyses_further_further_question2c
        self.confirmatory_analyses_further_further_question3c = confirmatory_analyses_further_further_question3c
        self.confirmatory_analyses_further_further_question4c = confirmatory_analyses_further_further_question4c
        self.confirmatory_analyses_further_further_question5c = confirmatory_analyses_further_further_question5c
        self.recommended_analysis_specify_question6c = recommended_analysis_specify_question6c
        self.recommended_analysis_specify_question7c = recommended_analysis_specify_question7c
        self.recommended_analysis_specify_question8c = recommended_analysis_specify_question8c
        self.recommended_analysis_specify_question9c = recommended_analysis_specify_question9c
        self.recommended_analysis_specify_question10c = recommended_analysis_specify_question10c
        self.recommended_analysis_specify_question11c = recommended_analysis_specify_question11c
        self.datacompletion = datacompletion
        self.looked = looked
        self.dataCollectionDates = dataCollectionDates
        self.additionalComments = additionalComments

    def to_object(self):
        
        return {
            "description_hypothesis_question1a": self.description_hypothesis_question1a,
            "description_hypothesis_question2a": self.description_hypothesis_question2a,
            "description_hypothesis_question3a": self.description_hypothesis_question3a,
            "description_hypothesis_question4a": self.description_hypothesis_question4a,
            "recommended_hypothesis_question5a": self.recommended_hypothesis_question5a,
            "recommended_hypothesis_question6a": self.recommended_hypothesis_question6a,
            "description_methods_design_question2a": self.description_methods_design_question2a,
            "description_methods_design_question2b": self.description_methods_design_question2b,
            "description_methods_design_question3b": self.description_methods_design_question3b,
            "description_methods_planned_sample_question4b": self.description_methods_planned_sample_question4b,
            "description_methods_planned_sample_question5b": self.description_methods_planned_sample_question5b,
            "description_methods_planned_sample_question6b": self.description_methods_planned_sample_question6b,
            "description_methods_planned_sample_question6b_upload": self.description_methods_planned_sample_question6b_upload,
            "description_methods_planned_sample_question7b": self.description_methods_planned_sample_question7b,
            "description_methods_exclusion_criteria_question8b": self.description_methods_exclusion_criteria_question8b,
            "description_methods_procedure_question10b": self.description_methods_procedure_question10b,
            "recommended_methods_procedure_question9b": self.recommended_methods_procedure_question9b,
            "recommended_methods_procedure_question9b_file": self.recommended_methods_procedure_question9b_file,
            "confirmatory_analyses_first_first_question1c": self.confirmatory_analyses_first_first_question1c,
            "confirmatory_analyses_first_first_question2c": self.confirmatory_analyses_first_first_question2c,
            "confirmatory_analyses_first_first_question3c": self.confirmatory_analyses_first_first_question3c,
            "confirmatory_analyses_first_first_question4c": self.confirmatory_analyses_first_first_question4c,
            "confirmatory_analyses_first_first_question5c": self.confirmatory_analyses_first_first_question5c,
            "confirmatory_analyses_second_second_question1c": self.confirmatory_analyses_second_second_question1c,
            "confirmatory_analyses_second_second_question2c": self.confirmatory_analyses_second_second_question2c,
            "confirmatory_analyses_second_second_question3c": self.confirmatory_analyses_second_second_question3c,
            "confirmatory_analyses_second_second_question4c": self.confirmatory_analyses_second_second_question4c,
            "confirmatory_analyses_second_second_question5c": self.confirmatory_analyses_second_second_question5c,
            "confirmatory_analyses_third_third_question1c": self.confirmatory_analyses_third_third_question1c,
            "confirmatory_analyses_third_third_question2c": self.confirmatory_analyses_third_third_question2c,
            "confirmatory_analyses_third_third_question3c": self.confirmatory_analyses_third_third_question3c,
            "confirmatory_analyses_third_third_question4c": self.confirmatory_analyses_third_third_question4c,
            "confirmatory_analyses_third_third_question5c": self.confirmatory_analyses_third_third_question5c,
            "confirmatory_analyses_fourth_fourth_question1c": self.confirmatory_analyses_fourth_fourth_question1c,
            "confirmatory_analyses_fourth_fourth_question2c": self.confirmatory_analyses_fourth_fourth_question2c,
            "confirmatory_analyses_fourth_fourth_question3c": self.confirmatory_analyses_fourth_fourth_question3c,
            "confirmatory_analyses_fourth_fourth_question4c": self.confirmatory_analyses_fourth_fourth_question4c,
            "confirmatory_analyses_fourth_fourth_question5c": self.confirmatory_analyses_fourth_fourth_question5c,
            "confirmatory_analyses_further_further_question1c": self.confirmatory_analyses_further_further_question1c,
            "confirmatory_analyses_further_further_question2c": self.confirmatory_analyses_further_further_question2c,
            "confirmatory_analyses_further_further_question3c": self.confirmatory_analyses_further_further_question3c,
            "confirmatory_analyses_further_further_question4c": self.confirmatory_analyses_further_further_question4c,
            "confirmatory_analyses_further_further_question5c": self.confirmatory_analyses_further_further_question5c,
            "recommended_analysis_specify_question6c": self.recommended_analysis_specify_question6c,
            "recommended_analysis_specify_question7c": self.recommended_analysis_specify_question7c,
            "recommended_analysis_specify_question8c": self.recommended_analysis_specify_question8c,
            "recommended_analysis_specify_question9c": self.recommended_analysis_specify_question9c,
            "recommended_analysis_specify_question10c": self.recommended_analysis_specify_question10c,
            "recommended_analysis_specify_question11c": self.recommended_analysis_specify_question11c,
            "datacompletion": self.datacompletion,
            "looked": self.looked,
            "dataCollectionDates": self.dataCollectionDates,
            "additionalComments": self.additionalComments
        }