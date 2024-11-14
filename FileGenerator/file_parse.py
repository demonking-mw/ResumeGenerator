import os
import csv

class FileAccMod:
    """
    File read and modify
    """
    def __init__(self, dominant_fp: str = 'ResumeGenerator/Informations/',
                 encoding: str = "utf-8") -> None:
        self.main_fp = dominant_fp
        self.encoding = encoding

    def construct_folder(
        self, section_filenames: list, section_folder_name: str,
        heading_top: int = 15, skills_top = 20, force_const: bool = False
    ) -> int:
        '''
        If the files exists, do nothing unless force_const is set to true
        returns the number of file added
        '''
        counter = 0
        for sect in section_filenames:
            sec = sect[:-4]
            fn = self.main_fp + section_folder_name + '/' + sect
            abs_file_path = os.path.abspath(fn)
            if (not os.path.isfile(abs_file_path)) or force_const:
                counter += 1
                with open(abs_file_path, mode='w', newline='', encoding=self.encoding) as file:
                    writer = csv.writer(file)
                    if sec == "HEADING":
                        writer.writerow(["HEADING", heading_top])
                    elif sec == "SKILLS":
                        writer.writerow(["SKILLS", skills_top])
                    else:
                        writer.writerow([sec])
        return counter

    def read_file(self, file_name: str, folder: str) -> list[list]:
        """
        Returns a csv file in the format of a 2d array
        """
        fn = self.main_fp + folder + "/" + file_name
        abs_file_path = os.path.abspath(fn)
        return list(csv.reader(open(abs_file_path, "r", encoding="utf-8")))

    def get_all(
        self, section_filenames: list, section_folder_name: str
    ) -> list[list[list]]:
        """
        Gets all the files provided in a 3d list:
        A list of 2d lists, each is a section
        """
        all_info = []
        for filename in section_filenames:
            all_info.append(self.read_file(filename, section_folder_name))
        return all_info

f = FileAccMod()
sf = ["HEADING.csv", "SKILLS.csv", "EDUCATION.csv", "EXPERIENCE.csv", "PROJECTS.csv"]
f.construct_folder(sf, "Strong", force_const=True)
