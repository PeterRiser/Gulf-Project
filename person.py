class Person:

    # attributes for each instance
    name=''
    category=''
    preferences={}

    # CONSTRUCTOR #
    # name is str of the user's name
    # category is str of identity group of user (i.e. gov't, public, etc.)
    # call helper function to set default preferences for person based on category type
    def __init__(self,name,category):
        self.name=name
        self.category=category
        self.set_preferences(category)


    def set_preferences(self,category):
        if (category=="local_county_gov"):
            self.preferences={'social_wellbeing':0.14,'economics':0.5,'community_action':0.04,'health':0.32,\
                          'vulnerable_populations':0.06,'environment_energy':0.03,'personal_impact':0.3,\
                          'response_following':0.13,'plans_planning':0.06,'information_needs':0.18,\
                          'communicating_with_stakeholders':0.08,'tools_resources_training':0.16,\
                          'short_term':0.44,'medium_term':0.22,'long_term':0.33}
        elif (category=="state_fed_gov"):
            self.preferences={'social_wellbeing':0.1,'economics':0.85,'community_action':0.05,'health':0.0,\
                          'vulnerable_populations':0.01,'environment_energy':0.07,'personal_impact':0.21,\
                          'response_following':0.26,'plans_planning':0.07,'information_needs':0.12,\
                          'communicating_with_stakeholders':0.22,'tools_resources_training':0.04,\
                          'short_term':0.68,'medium_term':0.22,'long_term':0.1}
        elif (category=="community_org"):
            self.preferences={'social_wellbeing':0.2,'economics':0.36,'community_action':0.08,'health':0.36,\
                          'vulnerable_populations':0.17,'environment_energy':0.06,'personal_impact':0.37,\
                          'response_following':0.05,'plans_planning':0.04,'information_needs':0.08,\
                          'communicating_with_stakeholders':0.09,'tools_resources_training':0.13,\
                          'short_term':0.3,'medium_term':0.24,'long_term':0.46}
        elif (category=="med_center"):
            self.preferences={'social_wellbeing':0.09,'economics':0.42,'community_action':0.15,'health':0.33,\
                          'vulnerable_populations':0.15,'environment_energy':0.0,'personal_impact':0.34,\
                          'response_following':0.07,'plans_planning':0.07,'information_needs':0.09,\
                          'communicating_with_stakeholders':0.21,'tools_resources_training':0.07,\
                          'short_term':0.6,'medium_term':0.27,'long_term':0.13}
        elif (category=="private_business"):
            self.preferences={'social_wellbeing':0.04,'economics':0.86,'community_action':0.11,'health':0.0,\
                          'vulnerable_populations':0.07,'environment_energy':0.04,'personal_impact':0.32,\
                          'response_following':0.07,'plans_planning':0.16,'information_needs':0.19,\
                          'communicating_with_stakeholders':0.11,'tools_resources_training':0.05,\
                          'short_term':0.57,'medium_term':0.29,'long_term':0.14}
        elif (category=="researcher"):
            self.preferences={'social_wellbeing':0.25,'economics':0.25,'community_action':0.25,'health':0.25,\
                          'vulnerable_populations':0.13,'environment_energy':0.13,'personal_impact':0.13,\
                          'response_following':0.13,'plans_planning':0.13,'information_needs':0.13,\
                          'communicating_with_stakeholders':0.13,'tools_resources_training':0.13,\
                          'short_term':0.33,'medium_term':0.33,'long_term':0.33}
        # category == "public"
        else:
            self.preferences={'social_wellbeing':0.25,'economics':0.25,'community_action':0.25,'health':0.25,\
                          'vulnerable_populations':0.13,'environment_energy':0.13,'personal_impact':0.13,\
                          'response_following':0.13,'plans_planning':0.13,'information_needs':0.13,\
                          'communicating_with_stakeholders':0.13,'tools_resources_training':0.13,\
                          'short_term':0.33,'medium_term':0.33,'long_term':0.33}

    def print_preferences(self):
        print(self.preferences)

    # key is str of keyword in preferences dictionary
    # new_weight is floating point of new value
    def set_weight(self,key,new_weight):
        self.preferences[key]=new_weight
