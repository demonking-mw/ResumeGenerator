"""
takes in the list of importance of attributes
returns a list with identical structure, but every weight should be changed
TO GET THIS WORKING: follow the beginner guide on the gpt official website
to get the key and store it in an env file, also put it in environment var.
"""
from openai import OpenAI

class GPT_Attribute:
    """
    set attribute list through gpt.
    """
    def get_gpt_out(self, input_message: list) -> str:
        """
        Gets the output from ChatGPT with a given input
        """
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=input_message)
        print("TOKEN_USED:")
        print(completion.usage.total_tokens)
        return completion.choices[0].message

    def set_simple(self, input_message: str) -> list:
        """
        makes the dictionary that gets fed into get_gpt_out
        """
        messages = [{
            "role": "user",
            "content": input_message
        }]
        return messages

    def get_job_description(self):
        """
        Can potentially be modded to implement web scraping
        """
        result = ""
        result += "JOB SUMMARY: "
        result += input("Please enter job summary:" + "\n")
        result += "JOB RESPONSIBILITIES: "
        result += input("Please enter job responsibility:" + "\n")
        result += "REQUIRED SKILL: "
        result += input("Please enter required skill:" + "\n")
        return result

    def get_init_prompt(self) -> list:
        """
        generates the first prompt for GPT
        """
        prompt = self.opening_line + "\n"
        prompt += "traits: ["
        for item in self.att_list:
            prompt += item[0] + ", "
        prompt += "]\n"
        prompt += self.answer_style_guide + "\n"
        prompt += self.att_list[0][0] + "=(your answer)"
        prompt += self.get_job_description()
        return self.set_simple(prompt)

    def search_in_result(self, gpt_result, target) -> int:
        """
        search for target attribute in some GPT result
        returns the attribute's value
        """
        # Find the index of the target string
        index = gpt_result.find(target)
        result = 1
        # Check if the target was found and if there is a character after it
        if index != -1 and index + len(target) < len(gpt_result):
            character_after_target = gpt_result[index + len(target)+1]
            print("DEBUG: CHAR_AFTER_TARGET is:")
            print(character_after_target)
            result = int(character_after_target)
        else:
            print("ERROR")
            print(f"Target: {target} not found in GPT result")
        return result

    def fill_list(self) -> list:
        """
        edits the att_list
        """
        result = []
        for item in self.att_list:
            value = self.search_in_result(self.first_response, item[0])
            result.append([item[0], value])
        return result

    def __init__(self, att_list: list[list]) -> None:
        self.att_list = att_list
        self.opening_line = "Analyze the following job description, give each trait/skill in the list below a value between 0 to 9, inclusive. The value reflects how much the skill helps in getting the job, and how much the recruiter would value the skill. You should also consider how relevant the skill is to the job, as skills in proximity to what the recruiter desires should be awarded with some value."
        self.answer_style_guide = "your response must cover each trait in the format of:"
        self.first_response_dic = self.get_gpt_out(self.get_init_prompt())
        print(self.first_response_dic)
        self.first_response = self.first_response_dic.content
        self.gpt_modded_list = self.fill_list()


