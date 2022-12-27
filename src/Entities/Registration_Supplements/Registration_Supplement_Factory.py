import json
from src.Entities.Registration_Supplements.Versions.AsPredicted_Preregistration import AsPredicted_Preregistration
from src.Entities.Registration_Supplements.Versions.Brandt_Replication_Pre_Registration import \
    Brandt_Replication_Pre_Registration
from src.Entities.Registration_Supplements.Versions.Empty_Registration_Supplement import \
    Empty_Registration_Supplement
from src.Entities.Registration_Supplements.Versions.OSF_Preregistration import OSF_Preregistration
from src.Entities.Registration_Supplements.Versions.OSF_Standard_Pre_Data_Collection_Registration import \
    OSF_Standard_Pre_Data_Collection_Registration
from src.Entities.Registration_Supplements.Versions.Open_Ended_Registration import Open_Ended_Registration
from src.Entities.Registration_Supplements.Versions.Pre_Registration_Social_Psychology import \
    Pre_Registration_Social_Psychology
from src.Entities.Registration_Supplements.Versions.Qualitative_Preregistration import Qualitative_Preregistration
from src.Entities.Registration_Supplements.Versions.Registered_Report_Protocol_Postregistration import \
    Registered_Report_Protocol_Postregistration
from src.Entities.Registration_Supplements.Versions.Registered_Report_Protocol_Preregistration import \
    Registered_Report_Protocol_Preregistration
from src.Entities.Registration_Supplements.Versions.Secondary_Data_Preregistration import \
    Secondary_Data_Preregistration


class Registration_Supplement_Factory:

    @staticmethod
    def create_registration_supplement(registration_supplement, registration_responses, entry):
        registration_supplement_obj = None

        if registration_supplement == "OSF Preregistration":
            if registration_responses:

                if "q2.question" in registration_responses:
                    hypotheses = registration_responses.get("q2.question")
                elif "q2" in registration_responses:
                    hypotheses = registration_responses.get("q2")
                else:
                    hypotheses = None

                if "q3.question" in registration_responses:
                    study_type = registration_responses.get("q3.question")
                elif "q3" in registration_responses:
                    study_type = registration_responses.get("q3")
                else:
                    study_type = None

                if "q4.question" in registration_responses:
                    blinding = registration_responses.get("q4.question")
                elif "q4" in registration_responses:
                    blinding = registration_responses.get("q4")
                else:
                    blinding = None

                if "q5.question" in registration_responses:
                    additional_blinding_information = registration_responses.get("q5.question")
                elif "q5" in registration_responses:
                    additional_blinding_information = registration_responses.get("q5")
                else:
                    additional_blinding_information = None

                if "q6.question" in registration_responses:
                    study_design = registration_responses.get("q6.question")
                elif "q6" in registration_responses:
                    study_design = registration_responses.get("q6")
                else:
                    study_design = None

                if "q7.question" in registration_responses:
                    randomization = registration_responses.get("q7.question")
                elif "q7" in registration_responses:
                    randomization = registration_responses.get("q7")
                else:
                    randomization = None

                if "q8.question" in registration_responses:
                    existing_data = registration_responses.get("q8.question")
                elif "q8" in registration_responses:
                    existing_data = registration_responses.get("q8")
                else:
                    existing_data = None

                if "q9.question" in registration_responses:
                    explanation_existing_data = registration_responses.get("q9.question")
                elif "q9" in registration_responses:
                    explanation_existing_data = registration_responses.get("q9")
                else:
                    explanation_existing_data = None

                if "q10.question" in registration_responses:
                    data_collection_procedures = registration_responses.get("q10.question")
                elif "q10" in registration_responses:
                    data_collection_procedures = registration_responses.get("q10")
                else:
                    data_collection_procedures = None

                if "q11.question" in registration_responses:
                    sample_size = registration_responses.get("q11.question")
                elif "q11" in registration_responses:
                    sample_size = registration_responses.get("q11")
                else:
                    sample_size = None

                if "q12.question" in registration_responses:
                    sample_size_rational = registration_responses.get("q12.question")
                elif "q12" in registration_responses:
                    sample_size_rational = registration_responses.get("q12")
                else:
                    sample_size_rational = None

                if "q13.question" in registration_responses:
                    stopping_rule = registration_responses.get("q13.question")
                elif "q13" in registration_responses:
                    stopping_rule = registration_responses.get("q13")
                else:
                    stopping_rule = None

                if "q14.question" in registration_responses:
                    manipulated_variables = registration_responses.get("q14.question")
                elif "q14" in registration_responses:
                    manipulated_variables = registration_responses.get("q14")
                else:
                    manipulated_variables = None

                if "q15.question" in registration_responses:
                    measured_variables = registration_responses.get("q15.question")
                elif "q15" in registration_responses:
                    measured_variables = registration_responses.get("q15")
                else:
                    measured_variables = None

                if "q16.question" in registration_responses:
                    indices = registration_responses.get("q16.question")
                elif "q16" in registration_responses:
                    indices = registration_responses.get("q16")
                else:
                    indices = None

                if "q17.question" in registration_responses:
                    statistical_models = registration_responses.get("q17.question")
                elif "q17" in registration_responses:
                    statistical_models = registration_responses.get("q17")
                else:
                    statistical_models = None

                if "q18.question" in registration_responses:
                    transformations = registration_responses.get("q18.question")
                elif "q18" in registration_responses:
                    transformations = registration_responses.get("q18")
                else:
                    transformations = None

                if "q19.question" in registration_responses:
                    inference_criteria = registration_responses.get("q19.question")
                elif "q19" in registration_responses:
                    inference_criteria = registration_responses.get("q19")
                else:
                    inference_criteria = None

                if "q20.question" in registration_responses:
                    data_exclusion = registration_responses.get("q20.question")
                elif "q20" in registration_responses:
                    data_exclusion = registration_responses.get("q20")
                else:
                    data_exclusion = None

                if "q21.question" in registration_responses:
                    missing_data = registration_responses.get("q21.question")
                elif "q21" in registration_responses:
                    missing_data = registration_responses.get("q21")
                else:
                    missing_data = None

                if "q22.question" in registration_responses:
                    exploratory_analysis = registration_responses.get("q22.question")
                elif "q22" in registration_responses:
                    exploratory_analysis = registration_responses.get("q22")
                else:
                    exploratory_analysis = None

                if "q23.question" in registration_responses:
                    other = registration_responses.get("q23.question")
                elif "q23" in registration_responses:
                    other = registration_responses.get("q23")
                else:
                    other = None

                registration_supplement_obj = OSF_Preregistration(hypotheses, study_type, blinding,
                                                                  additional_blinding_information, study_design,
                                                                  randomization,
                                                                  existing_data, explanation_existing_data,
                                                                  data_collection_procedures, sample_size,
                                                                  sample_size_rational,
                                                                  stopping_rule, manipulated_variables,
                                                                  measured_variables, indices, statistical_models,
                                                                  transformations,
                                                                  inference_criteria, data_exclusion, missing_data,
                                                                  exploratory_analysis, other)


        elif registration_supplement == "Open-Ended Registration":
            if registration_responses:
                summary = registration_responses.get("summary")

                registration_supplement_obj = Open_Ended_Registration(summary)


        elif registration_supplement == "Secondary Data Preregistration":
            if registration_responses:
                if "q1.question" in registration_responses:
                    research_question = registration_responses.get("q1.question")
                elif "q1" in registration_responses:
                    research_question = registration_responses.get("q1")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q2.question" in registration_responses:
                    hypotheses = registration_responses.get("q2.question")
                elif "q2" in registration_responses:
                    hypotheses = registration_responses.get("q2")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q3.question" in registration_responses:
                    dataset = registration_responses.get("q3.question")
                elif "q3" in registration_responses:
                    dataset = registration_responses.get("q3")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q4.question" in registration_responses:
                    dataset_availability = registration_responses.get("q4.question")
                elif "q4" in registration_responses:
                    dataset_availability = registration_responses.get("q4")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q5.question" in registration_responses:
                    data_access = registration_responses.get("q5.question")
                elif "q5" in registration_responses:
                    data_access = registration_responses.get("q5")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q6.question" in registration_responses:
                    data_identifiers = registration_responses.get("q6.question")
                elif "q6" in registration_responses:
                    data_identifiers = registration_responses.get("q6")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q7.question" in registration_responses:
                    access_date = registration_responses.get("q7.question")
                elif "q7" in registration_responses:
                    access_date = registration_responses.get("q7")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q8.question" in registration_responses:
                    data_collection_procedure = registration_responses.get("q8.question")
                elif "q8" in registration_responses:
                    data_collection_procedure = registration_responses.get("q8")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q10.question" in registration_responses:
                    codebook = registration_responses.get("q10.question")
                elif "q10" in registration_responses:
                    codebook = registration_responses.get("q10")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q12.question" in registration_responses:
                    manipulated_variables = registration_responses.get("q12.question")
                elif "q12" in registration_responses:
                    manipulated_variables = registration_responses.get("q12")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q14.question" in registration_responses:
                    measured_variables = registration_responses.get("q14.question")
                elif "q14" in registration_responses:
                    measured_variables = registration_responses.get("q14")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q15.question" in registration_responses:
                    units_of_analysis = registration_responses.get("q15.question")
                elif "q15" in registration_responses:
                    units_of_analysis = registration_responses.get("q15")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q16.question" in registration_responses:
                    missing_data = registration_responses.get("q16.question")
                elif "q16" in registration_responses:
                    missing_data = registration_responses.get("q16")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q17.question" in registration_responses:
                    statistical_outlier = registration_responses.get("q17.question")
                elif "q17" in registration_responses:
                    statistical_outlier = registration_responses.get("q17")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q18.question" in registration_responses:
                    sampling_weights = registration_responses.get("q18.question")
                elif "q18" in registration_responses:
                    sampling_weights = registration_responses.get("q18")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q19.question" in registration_responses:
                    work_references = registration_responses.get("q19.question")
                elif "q19" in registration_responses:
                    work_references = registration_responses.get("q19")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q20.question" in registration_responses:
                    prior_knowledge = registration_responses.get("q20.question")
                elif "q20" in registration_responses:
                    prior_knowledge = registration_responses.get("q20")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q21.question" in registration_responses:
                    statistical_model = registration_responses.get("q21.question")
                elif "q21" in registration_responses:
                    statistical_model = registration_responses.get("q21")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q22.question" in registration_responses:
                    effect_size = registration_responses.get("q22.question")
                elif "q22" in registration_responses:
                    effect_size = registration_responses.get("q22")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q23.question" in registration_responses:
                    statistical_power = registration_responses.get("q23.question")
                elif "q23" in registration_responses:
                    statistical_power = registration_responses.get("q23")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q24.question" in registration_responses:
                    inference_criteria = registration_responses.get("q24.question")
                elif "q24" in registration_responses:
                    inference_criteria = registration_responses.get("q24")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q25.question" in registration_responses:
                    data_problems = registration_responses.get("q25.question")
                elif "q25" in registration_responses:
                    data_problems = registration_responses.get("q25")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q26.question" in registration_responses:
                    hypothesis_test = registration_responses.get("q26.question")
                elif "q26" in registration_responses:
                    hypothesis_test = registration_responses.get("q26")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q27.question" in registration_responses:
                    exploratory_analysis = registration_responses.get("q27.question")
                elif "q27" in registration_responses:
                    exploratory_analysis = registration_responses.get("q27")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                registration_supplement_obj = Secondary_Data_Preregistration(research_question, hypotheses, dataset,
                                                                             dataset_availability, data_access,
                                                                             data_identifiers,
                                                                             access_date, data_collection_procedure,
                                                                             codebook, manipulated_variables,
                                                                             measured_variables,
                                                                             units_of_analysis, missing_data,
                                                                             statistical_outlier, sampling_weights,
                                                                             work_references,
                                                                             prior_knowledge, statistical_model,
                                                                             effect_size, statistical_power,
                                                                             inference_criteria, data_problems,
                                                                             hypothesis_test, exploratory_analysis)


        elif registration_supplement == "Qualitative Preregistration":
            if registration_responses:
                if "q1.question" in registration_responses:
                    research_aim = registration_responses.get("q1.question")
                elif "q1" in registration_responses:
                    research_aim = registration_responses.get("q1")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q2.question" in registration_responses:
                    type_research_aim = registration_responses.get("q2.question")
                elif "q2" in registration_responses:
                    type_research_aim = registration_responses.get("q2")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q3.question" in registration_responses:
                    research_question = registration_responses.get("q3.question")
                elif "q3" in registration_responses:
                    research_question = registration_responses.get("q3")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q4.question" in registration_responses:
                    anticipated_duration = registration_responses.get("q4.question")
                elif "q4" in registration_responses:
                    anticipated_duration = registration_responses.get("q4")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q5.question" in registration_responses:
                    study_design = registration_responses.get("q5.question")
                elif "q5" in registration_responses:
                    study_design = registration_responses.get("q5")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q6.question" in registration_responses:
                    sampling_case_selection_strategy = registration_responses.get("q6.question")
                elif "q6" in registration_responses:
                    sampling_case_selection_strategy = registration_responses.get("q6")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q7.question" in registration_responses:
                    data_source = registration_responses.get("q7.question")
                elif "q7" in registration_responses:
                    data_source = registration_responses.get("q7")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q8.question" in registration_responses:
                    data_collection_methods = registration_responses.get("q8.question")
                elif "q8" in registration_responses:
                    data_collection_methods = registration_responses.get("q8")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q9.question" in registration_responses:
                    data_collection_tools = registration_responses.get("q9.question")
                elif "q9" in registration_responses:
                    data_collection_tools = registration_responses.get("q9")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q10.question" in registration_responses:
                    stopping_criteria = registration_responses.get("q10.question")
                elif "q10" in registration_responses:
                    stopping_criteria = registration_responses.get("q10")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q11.question" in registration_responses:
                    data_analysis_approach = registration_responses.get("q11.question")
                elif "q11" in registration_responses:
                    data_analysis_approach = registration_responses.get("q11")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q12.question" in registration_responses:
                    data_analysis_process = registration_responses.get("q12.question")
                elif "q12" in registration_responses:
                    data_analysis_process = registration_responses.get("q12")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q13.question" in registration_responses:
                    credibility_strategies = registration_responses.get("q13.question")
                elif "q13" in registration_responses:
                    credibility_strategies = registration_responses.get("q13")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q14.question" in registration_responses:
                    rationale = registration_responses.get("q14.question")
                elif "q14" in registration_responses:
                    rationale = registration_responses.get("q14")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                if "q15.question" in registration_responses:
                    reflection_positionality = registration_responses.get("q15.question")
                elif "q15" in registration_responses:
                    reflection_positionality = registration_responses.get("q15")
                else:
                    raise Exception(json.dumps(entry, indent=4))

                registration_supplement_obj = Qualitative_Preregistration(research_aim, type_research_aim,
                                                                          research_question, anticipated_duration,
                                                                          study_design,
                                                                          sampling_case_selection_strategy, data_source,
                                                                          data_collection_methods,
                                                                          data_collection_tools,
                                                                          stopping_criteria, data_analysis_approach,
                                                                          data_analysis_process, credibility_strategies,
                                                                          rationale,
                                                                          reflection_positionality)


        elif registration_supplement == "Preregistration Template from AsPredicted.org":

            if registration_responses:
                data = registration_responses.get("data")
                hypothesis = registration_responses.get("hypothesis")
                dependent = registration_responses.get("dependent")
                conditions = registration_responses.get("conditions")
                analyses = registration_responses.get("analyses")
                outliers = registration_responses.get("outliers")
                sample = registration_responses.get("sample")
                other = registration_responses.get("other")
                name = registration_responses.get("name")
                study_type = registration_responses.get("study_type")
                study_type_other = registration_responses.get("study_type_other")

                registration_supplement_obj = AsPredicted_Preregistration(data, hypothesis, dependent, conditions,
                                                                          analyses, outliers, sample, other, name,
                                                                          study_type,
                                                                          study_type_other)


        elif registration_supplement == "OSF-Standard Pre-Data Collection Registration":
            if registration_responses:
                datacompletion = registration_responses.get("datacompletion")
                looked = registration_responses.get("looked")
                comments = registration_responses.get("comments")

                registration_supplement_obj = OSF_Standard_Pre_Data_Collection_Registration(datacompletion, looked,
                                                                                            comments)

        elif registration_supplement == "Pre-Registration in Social Psychology (van 't Veer & Giner-Sorolla, 2016): Pre-Registration":
            if registration_responses:
                description_hypothesis_question1a = registration_responses.get("description-hypothesis.question1a")
                description_hypothesis_question2a = registration_responses.get("description-hypothesis.question2a")
                description_hypothesis_question3a = registration_responses.get("description-hypothesis.question3a")

                if "description-hypothesis.question4a" in registration_responses:
                    description_hypothesis_question4a = registration_responses.get("description-hypothesis.question4a")
                else:
                    description_hypothesis_question4a = None

                recommended_hypothesis_question5a = registration_responses.get("recommended-hypothesis.question5a")
                recommended_hypothesis_question6a = registration_responses.get("recommended-hypothesis.question6a")
                description_methods_design_question2a = registration_responses.get("description-methods.design.question2a")
                description_methods_design_question2b = registration_responses.get("description-methods.design.question2b")
                description_methods_design_question3b = registration_responses.get("description-methods.design.question3b")
                description_methods_planned_sample_question4b = registration_responses.get(
                    "description-methods.planned-sample.question4b")
                description_methods_planned_sample_question5b = registration_responses.get(
                    "description-methods.planned-sample.question5b")
                description_methods_planned_sample_question6b = registration_responses.get(
                    "description-methods.planned-sample.question6b")
                description_methods_planned_sample_question6b_upload = registration_responses.get(
                    "description-methods.planned-sample.question6b-upload")
                description_methods_planned_sample_question7b = registration_responses.get(
                    "description-methods.planned-sample.question7b")
                description_methods_exclusion_criteria_question8b = registration_responses.get(
                    "description-methods.exclusion-criteria.question8b")
                description_methods_procedure_question10b = registration_responses.get(
                    "description-methods.procedure.question10b")
                recommended_methods_procedure_question9b = registration_responses.get(
                    "recommended-methods.procedure.question9b")
                recommended_methods_procedure_question9b_file = registration_responses.get(
                    "recommended-methods.procedure.question9b-file")
                confirmatory_analyses_first_first_question1c = registration_responses.get(
                    "confirmatory-analyses-first.first.question1c")
                confirmatory_analyses_first_first_question2c = registration_responses.get(
                    "confirmatory-analyses-first.first.question2c")
                confirmatory_analyses_first_first_question3c = registration_responses.get(
                    "confirmatory-analyses-first.first.question3c")
                confirmatory_analyses_first_first_question4c = registration_responses.get(
                    "confirmatory-analyses-first.first.question4c")
                confirmatory_analyses_first_first_question5c = registration_responses.get(
                    "confirmatory-analyses-first.first.question5c")
                confirmatory_analyses_second_second_question1c = registration_responses.get(
                    "confirmatory-analyses-second.second.question1c")
                confirmatory_analyses_second_second_question2c = registration_responses.get(
                    "confirmatory-analyses-second.second.question2c")
                confirmatory_analyses_second_second_question3c = registration_responses.get(
                    "confirmatory-analyses-second.second.question3c")
                confirmatory_analyses_second_second_question4c = registration_responses.get(
                    "confirmatory-analyses-second.second.question4c")
                confirmatory_analyses_second_second_question5c = registration_responses.get(
                    "confirmatory-analyses-second.second.question5c")
                confirmatory_analyses_third_third_question1c = registration_responses.get(
                    "confirmatory-analyses-third.third.question1c")
                confirmatory_analyses_third_third_question2c = registration_responses.get(
                    "confirmatory-analyses-third.third.question2c")
                confirmatory_analyses_third_third_question3c = registration_responses.get(
                    "confirmatory-analyses-third.third.question3c")
                confirmatory_analyses_third_third_question4c = registration_responses.get(
                    "confirmatory-analyses-third.third.question4c")
                confirmatory_analyses_third_third_question5c = registration_responses.get(
                    "confirmatory-analyses-third.third.question5c")
                confirmatory_analyses_fourth_fourth_question1c = registration_responses.get(
                    "confirmatory-analyses-fourth.fourth.question1c")
                confirmatory_analyses_fourth_fourth_question2c = registration_responses.get(
                    "confirmatory-analyses-fourth.fourth.question2c")
                confirmatory_analyses_fourth_fourth_question3c = registration_responses.get(
                    "confirmatory-analyses-fourth.fourth.question3c")
                confirmatory_analyses_fourth_fourth_question4c = registration_responses.get(
                    "confirmatory-analyses-fourth.fourth.question4c")
                confirmatory_analyses_fourth_fourth_question5c = registration_responses.get(
                    "confirmatory-analyses-fourth.fourth.question5c")
                confirmatory_analyses_further_further_question1c = registration_responses.get(
                    "confirmatory-analyses-further.further.question1c")
                confirmatory_analyses_further_further_question2c = registration_responses.get(
                    "confirmatory-analyses-further.further.question2c")
                confirmatory_analyses_further_further_question3c = registration_responses.get(
                    "confirmatory-analyses-further.further.question3c")
                confirmatory_analyses_further_further_question4c = registration_responses.get(
                    "confirmatory-analyses-further.further.question4c")
                confirmatory_analyses_further_further_question5c = registration_responses.get(
                    "confirmatory-analyses-further.further.question5c")
                recommended_analysis_specify_question6c = registration_responses.get(
                    "recommended-analysis.specify.question6c")
                recommended_analysis_specify_question7c = registration_responses.get(
                    "recommended-analysis.specify.question7c")
                recommended_analysis_specify_question8c = registration_responses.get(
                    "recommended-analysis.specify.question8c")
                recommended_analysis_specify_question9c = registration_responses.get(
                    "recommended-analysis.specify.question9c")
                recommended_analysis_specify_question10c = registration_responses.get(
                    "recommended-analysis.specify.question10c")
                recommended_analysis_specify_question11c = registration_responses.get(
                    "recommended-analysis.specify.question11c")
                datacompletion = registration_responses.get("datacompletion")
                looked = registration_responses.get("looked")
                dataCollectionDates = registration_responses.get("dataCollectionDates")
                additionalComments = registration_responses.get("additionalComments")

                registration_supplement_obj = Pre_Registration_Social_Psychology(description_hypothesis_question1a,
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
                                                                                 additionalComments)


        elif registration_supplement == "Replication Recipe (Brandt et al., 2013): Pre-Registration":
            if registration_responses:
                effect_description = registration_responses.get("item1")
                effect_importance = registration_responses.get("item2")
                effect_size = registration_responses.get("item3")
                confidence_interval = registration_responses.get("item4")
                sample_size = registration_responses.get("item5")
                location = registration_responses.get("item6")
                country = registration_responses.get("item7")
                sample = registration_responses.get("item8")
                medium = registration_responses.get("item9")
                availability_original_material = registration_responses.get("item10")
                original_assumptions_hold = registration_responses.get("item11")
                location_data_collection = registration_responses.get("item12")
                knowledge_experimental_condition = registration_responses.get("item13")
                knowledge_overall_hypotheses = registration_responses.get("item14")
                target_sample_size = registration_responses.get("item15")
                rationale_sample_size = registration_responses.get("item16")
                sim_instruction = registration_responses.get("item17")
                sim_measures = registration_responses.get("item18")
                sim_stimuli = registration_responses.get("item19")
                sim_procedure = registration_responses.get("item20")
                sim_location = registration_responses.get("item21")
                sim_remuneration = registration_responses.get("item22")
                sim_population = registration_responses.get("item23")
                dif_study = registration_responses.get("item24")
                test_prev_steps = registration_responses.get("item25")
                exclusion_criteria = registration_responses.get("item26")
                analysis_plan = registration_responses.get("item27")
                successful_replication_def = registration_responses.get("item28")

                registration_supplement_obj = Brandt_Replication_Pre_Registration(effect_description, effect_importance,
                                                                                  effect_size, confidence_interval,
                                                                                  sample_size,
                                                                                  location, country, sample, medium,
                                                                                  availability_original_material,
                                                                                  original_assumptions_hold,
                                                                                  location_data_collection,
                                                                                  knowledge_experimental_condition,
                                                                                  knowledge_overall_hypotheses,
                                                                                  target_sample_size,
                                                                                  rationale_sample_size,
                                                                                  sim_instruction, sim_measures,
                                                                                  sim_stimuli, sim_procedure,
                                                                                  sim_location, sim_remuneration,
                                                                                  sim_population, dif_study,
                                                                                  test_prev_steps, exclusion_criteria,
                                                                                  analysis_plan,
                                                                                  successful_replication_def)

        elif registration_supplement == "Registered Report Protocol Preregistration":
            if registration_responses:
                in_principle_acceptance = registration_responses.get("q2")
                journal_title = registration_responses.get("q3")
                date_in_principle_acceptance = registration_responses.get("q4")
                other = registration_responses.get("q6")

                registration_supplement_obj = Registered_Report_Protocol_Preregistration(in_principle_acceptance,
                                                                                         journal_title,
                                                                                         date_in_principle_acceptance,
                                                                                         other)


        elif registration_supplement == "Replication Recipe (Brandt et al., 2013): Post-Completion":
            if registration_responses:

                final_design = registration_responses.get("item29")
                effect_size = registration_responses.get("item30")
                confidence_interval = registration_responses.get("item31")
                replication_effect_size = registration_responses.get("item32")
                replication_judgment = registration_responses.get("item33")
                replication_judgment_reason = registration_responses.get("item34")
                data = registration_responses.get("item35")
                analyses = registration_responses.get("item36")
                limitations = registration_responses.get("item37")

                registration_supplement_obj = Registered_Report_Protocol_Postregistration(final_design, effect_size, confidence_interval, replication_effect_size, replication_judgment,
                 replication_judgment_reason, data, analyses, limitations)


        # else:
        #     print(registration_supplement)
        #     print("##")

        if registration_supplement_obj:
            return registration_supplement_obj
        else:
            return Empty_Registration_Supplement()
