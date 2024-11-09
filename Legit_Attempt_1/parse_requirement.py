"""
Parse the requirement of a given job post and gives a list to the resume_info file
Goal: integrate chatgpt
"""


class ParseReq:
    """

    """


    def __init__(self, skills_att_list: list[list], sections_mega_list: list) -> None:
        """
        Skills_att_list includes the list skills, alongside with each attribute

        [s1, [a1, a2, a3]
        s2, [a1, a2, a3]
        ,...]

        sections_mega_list includes a list of section_attribute_list
        each section_attribute_list:

        [[[['PROGRAMMING', 9], ['JAVA', 8]], height1],
         [[['PROGRAMMING', 9], ['JAVA', 8]], height2],
         ...
         ]
        
        section_mega_list is a list of that shit, thus its a super CHONK thing
        """
        self.skills_att_list = skills_att_list
        self.sections_mega_list = sections_mega_list
        self.all_att_in_skills = self.get_all_skills_att()
        self.desired_skillset = self.get_desire()
        
        
