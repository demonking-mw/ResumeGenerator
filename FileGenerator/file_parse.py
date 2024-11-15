'''
Parse files. 
file modification functions also implemented here
'''
import os
import csv

class FileAccMod:
    """
    File read and modify
    """
    def __init__(self, dominant_fp: str = 'Informations/',
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
        return list(csv.reader(open(abs_file_path, "r", encoding=self.encoding)))

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

    def add_line_ss(
        self,
        attribute_list: list[list],
        folder_name: str,
        file_name: str,
        header: str,
        time: str,
        descriptions: list,
        location: int = 0,
    ):
        '''
        add a line to a standard section. note: each item in attribute_list is a [str, int]
        location describes where the item is put relative to other ones
        enter an arbitrarily large number for location for the item to be placed last (say, 1000000)
        '''
        content = self.read_file(file_name, folder_name)
        new_att = []
        for att in attribute_list:
            curr_att = "/=-z+f]j " + str(att[0]) + " " + str(att[1])
            new_att.append(curr_att)
        new_att.append(header)
        new_att.append(time)
        for desc in descriptions:
            new_att.append(desc)
        if location+1 > len(content):
            location = len(content)-1
        content.insert(location+1, new_att)

        fn = self.main_fp + folder_name + '/' + file_name
        abs_file_path = os.path.abspath(fn)
        with open(abs_file_path, mode="w", newline="", encoding=self.encoding) as file:
            writer = csv.writer(file)
            writer.writerows(content)
