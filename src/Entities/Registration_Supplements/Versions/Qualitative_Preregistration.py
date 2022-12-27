
class Qualitative_Preregistration:

    def __init__(self, research_aim, type_research_aim, research_question, anticipated_duration, study_design,
                 sampling_case_selection_strategy, data_source, data_collection_methods, data_collection_tools,
                 stopping_criteria, data_analysis_approach, data_analysis_process, credibility_strategies, rationale,
                 reflection_positionality):

        self.research_aim = research_aim
        self.type_research_aim = type_research_aim
        self.research_question = research_question
        self.anticipated_duration = anticipated_duration
        self.study_design = study_design
        self.sampling_case_selection_strategy = sampling_case_selection_strategy
        self.data_source = data_source
        self.data_collection_methods = data_collection_methods
        self.data_collection_tools = data_collection_tools
        self.stopping_criteria = stopping_criteria
        self.data_analysis_approach = data_analysis_approach
        self.data_analysis_process = data_analysis_process
        self.credibility_strategies = credibility_strategies
        self.rationale = rationale
        self.reflection_positionality = reflection_positionality

    def to_object(self):
        return {
            "research_aim": self.research_aim,
            "type_research_aim": self.type_research_aim,
            "research_question": self.research_question,
            "anticipated_duration": self.anticipated_duration,
            "study_design": self.study_design,
            "sampling_case_selection_strategy": self.sampling_case_selection_strategy,
            "data_source": self.data_source,
            "data_collection_methods": self.data_collection_methods,
            "data_collection_tools": self.data_collection_tools,
            "stopping_criteria": self.stopping_criteria,
            "data_analysis_approach": self.data_analysis_approach,
            "data_analysis_process": self.data_analysis_process,
            "credibility_strategies": self.credibility_strategies,
            "rationale": self.rationale,
            "reflection_positionality": self.reflection_positionality
        }