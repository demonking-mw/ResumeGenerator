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
    def __init__(self, dominant_fp: str = 'ResumeGenerator/Informations/',
                 encoding: str = "utf-8") -> None:
        self.main_fp = dominant_fp
        self.encoding = encoding

    def change_header(self, folder_name: str, person_name: str="", head_desc: str="") -> str:
        '''
        changes the header. Filename is not requried since it just changes header
        the return is the status: success or error
        '''
        try:
            curr_file = self.read_file("HEADING.csv", folder_name)
            print(curr_file)
            if curr_file[0][0] != "HEADING":
                return "Wrong file: header is instead " + curr_file[0][1]
            new_row = []
            if person_name != "":
                new_row.append(person_name)
            else:
                new_row.append(curr_file[1][0])
            if head_desc != "":
                new_row.append(head_desc)
            else:
                new_row.append(curr_file[1][1])
            if len(curr_file) == 1:
                new_row.append(str(20))
                curr_file.append(new_row)
            else:
                new_row.append(curr_file[1][2])
                curr_file[1] = new_row
            fn = self.main_fp + folder_name + "/" + "HEADING.csv"
            abs_file_path = os.path.abspath(fn)
            with open(abs_file_path, mode="w", newline="", encoding=self.encoding) as file:
                writer = csv.writer(file)
                writer.writerows(curr_file)
            return "completed!"
        except Exception as error:
            return str(error)

    def print_folder(self, folder_name, file_name):
        '''
        returns
        '''
        curr = self.read_file(file_name, folder_name)
        result = ""
        nx = "\n"
        bk = "\n\n"
        result += curr[0][0]+bk
        for i in range(1, len(curr)):
            formatted = self.style_disp_item_ss(curr[i])
            for item in formatted:
                result += item+nx
            result += bk
        return result
        

    def style_disp_item_ss(self, raw_list: list, brief: bool = False) -> list:
        '''
        Style an item for display
        Ideally, each item in the list occupies a line
        '''
        title_info = ""
        time_info = ""
        information_list = []
        traits_list = []
        for item in raw_list:
            splitted = item.split()
            if len(splitted) > 0 and splitted[0] == "/=-z+f]j":
                traits_list.append([splitted[1], splitted[2]])
                continue
            if title_info == "":
                title_info = item
                continue
            if time_info == "":
                time_info = item
                continue
            information_list.append(item)
        
        result_list = []
        result_list.append(title_info + "   ---   " + time_info) 
        if brief:
            return result_list
        for info in information_list:
            result_list.append(info)
        result_list.append("Traits:")
        for info in traits_list:
            result_list.append(str(info[0]) + "   ->   " + str(info[1]))
        return result_list

    def del_by_header_ss(self, folder_name: str, file_name: str, target_header: str) -> tuple[list, bool]:
        '''
        Delete an item in the file and return its information 
        '''
        content = self.read_file(file_name, folder_name)
        row = 1
        target_row_header = None
        target_row_index = []
        while row < len(content):
            # loop through each row of the resume
            col = 0
            for item in content[row]:
                splitted = item.split()
                if len(splitted) > 0 and splitted[0] == "/=-z+f]j":
                    col += 1
                else:
                    break
            if target_header in content[row][col]:
                target_row_index.append(row)
                target_row_header = content[row][col]
            row += 1
        deleted_result = []
        success = False
        if len(target_row_index) == 0:
            # FRONTEND: do something here since target is not found
            print(target_header + " NOT FOUND IN FILE " + file_name)
            deleted_result = ["Not Found"]
        elif len(target_row_index) == 1:
            # FRONTEND: found row
            deleted_result = content[target_row_index[0]]
            content.pop(target_row_index[0])
            success = True
        else:
            # FRONTEND: multiple items found, alert user
            print("MULTIPLE ITEMS FOUND ON REPLACE ATTEMPT, REPLACE CANCELLED")
            deleted_result = ["Multiple Found"]
        fn = self.main_fp + folder_name + "/" + file_name
        abs_file_path = os.path.abspath(fn)
        with open(abs_file_path, mode="w", newline="", encoding=self.encoding) as file:
            writer = csv.writer(file)
            writer.writerows(content)

    def mod_by_header_ss(self,
        attribute_list: list[list],
        folder_name: str,
        file_name: str,
        target_header: str,
        time: str,
        descriptions: list) -> None:
        '''
        Modify an item in the file by searching for its header
        '''
        content = self.read_file(file_name, folder_name)
        row = 1
        target_row_header = None
        target_row_index = []
        while row < len(content):
            # loop through each row of the resume
            col = 0
            for item in content[row]:
                splitted = item.split()
                if len(splitted) > 0 and splitted[0] == "/=-z+f]j":
                    col+=1
                else:
                    break
            if target_header in content[row][col]:
                target_row_index.append(row)
                target_row_header = content[row][col]
            row+=1
        if len(target_row_index) == 0:
            # FRONTEND: do something here since target is not found
            print(target_header + " NOT FOUND IN FILE " + file_name)
        elif len(target_row_index) == 1:
            # FRONTEND: found row
            new_att = []
            for att in attribute_list:
                curr_att = "/=-z+f]j " + str(att[0]) + " " + str(att[1])
                new_att.append(curr_att)
            new_att.append(target_row_header)
            new_att.append(time)
            for desc in descriptions:
                new_att.append(desc)
            content.pop(target_row_index[0])
            content.insert(target_row_index[0], new_att)
        else:
            # FRONTEND: multiple items found, alert user
            print("MULTIPLE ITEMS FOUND ON REPLACE ATTEMPT, REPLACE CANCELLED")
        fn = self.main_fp + folder_name + "/" + file_name
        abs_file_path = os.path.abspath(fn)
        with open(abs_file_path, mode="w", newline="", encoding=self.encoding) as file:
            writer = csv.writer(file)
            writer.writerows(content)

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

