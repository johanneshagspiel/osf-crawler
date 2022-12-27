
class Brandt_Replication_Pre_Registration:

    def __init__(self, effect_description, effect_importance, effect_size, confidence_interval, sample_size,
                 location, country, sample, medium, availability_original_material, original_assumptions_hold,
                 location_data_collection, knowledge_experimental_condition, knowledge_overall_hypotheses,
                 target_sample_size, rationale_sample_size, sim_instruction, sim_measures, sim_stimuli, sim_procedure,
                 sim_location, sim_remuneration, sim_population, dif_study, test_prev_steps, exclusion_criteria,
                 analysis_plan, successful_replication_def):

        self.effect_description = effect_description
        self.effect_importance = effect_importance
        self.effect_size = effect_size
        self.confidence_interval = confidence_interval,
        self.sample_size = sample_size
        self.location = location
        self.country = country
        self.sample = sample
        self.medium = medium
        self.availability_original_material = availability_original_material
        self.original_assumptions_hold = original_assumptions_hold
        self.location_data_collection = location_data_collection
        self.knowledge_experimental_condition = knowledge_experimental_condition
        self.knowledge_overall_hypotheses = knowledge_overall_hypotheses
        self.target_sample_size = target_sample_size
        self.rationale_sample_size = rationale_sample_size
        self.sim_instruction = sim_instruction
        self.sim_measures = sim_measures
        self.sim_stimuli = sim_stimuli
        self.sim_procedure = sim_procedure
        self.sim_location = sim_location
        self.sim_remuneration = sim_remuneration
        self.sim_population = sim_population
        self.dif_study = dif_study
        self.test_prev_steps = test_prev_steps
        self.exclusion_criteria = exclusion_criteria
        self.analysis_plan = analysis_plan
        self.successful_replication_def = successful_replication_def

    def to_object(self):
        return {
            "effect_description": self.effect_description,
            "effect_importance": self.effect_importance,
            "effect_size": self.effect_size,
            "confidence_interval": self.confidence_interval,
            "sample_size": self.sample_size,
            "location": self.location,
            "country": self.country,
            "sample": self.sample,
            "medium": self.medium,
            "availability_original_material": self.availability_original_material,
            "original_assumptions_hold": self.original_assumptions_hold,
            "location_data_collection": self.location_data_collection,
            "knowledge_experimental_condition": self.knowledge_experimental_condition,
            "knowledge_overall_hypotheses": self.knowledge_overall_hypotheses,
            "target_sample_size": self.target_sample_size,
            "rationale_sample_size": self.rationale_sample_size,
            "sim_instruction": self.sim_instruction,
            "sim_measures": self.sim_measures,
            "sim_stimuli": self.sim_stimuli,
            "sim_procedure": self.sim_procedure,
            "sim_location": self.sim_location,
            "sim_remuneration": self.sim_remuneration,
            "sim_population": self.sim_population,
            "dif_study": self.dif_study,
            "test_prev_steps": self.test_prev_steps,
            "exclusion_criteria": self.exclusion_criteria,
            "analysis_plan": self.analysis_plan,
            "successful_replication_def": self.successful_replication_def
        }