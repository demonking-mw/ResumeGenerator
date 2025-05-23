"""
A standard section of the resume in the format of "EXPERIENCE" tab
"""

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth

from . import styles
from . import style_info


class StandardSection:
    """
    Contains all the information to build a section of the resume
    To define it: the __init__ takes:
    title, list[list[str]], XXX_font: fonts, XXX_margin: int
    PENDING TASK: finish up this such that every styling is in terms of StyleInfo
    """

        # style
    #######################################################################
    

    #__DEFAULT_SIDE_MARGIN = 20
    #__DEFAULT_TOP_MARGIN = 5
    #__DEFAULT_HEIGHT_BUFFER = 10
    #__WRAP_FORGIVE = 20
    #######################################################################


    def __init__(
        self,
        title: str,
        all_info: list[list],
        sec_style: style_info.StyleInfo=None,
        bullet_point: bool = False,
    ) -> None:
        if sec_style is None:
            sec_style = styles.ALlStyles().resume_style_0.subsections[title]
        
        self.title = title
        self.raw_info_list = all_info
        self.attribute_weight_list = []
        
        self.section_style = sec_style
        #self.all_fonts = fonts.AllFonts()
        
        self.font_title_style = self.section_style.subsections["title_font"]
        self.font_title = self.font_title_style.get_paragraph_style()
        #self.font_title = self.all_fonts.name_font
        
        self.font_subtitle_style = self.section_style.subsections["subtitle_font"]
        self.font_subtitle = self.font_subtitle_style.get_paragraph_style()
        #self.font_subtitle = self.all_fonts.subsection_title
        
        self.font_subright_style = self.section_style.subsections["subright_font"]
        self.font_subright = self.font_subright_style.get_paragraph_style()
        #self.font_subright = self.all_fonts.subright_title
        
        self.font_text_style = self.section_style.subsections["standard_text_font"]
        self.font_text = self.font_text_style.get_paragraph_style()
       # self.font_text = self.all_fonts.text_font_standard_sec
       
        self.side_margin = self.section_style.section_attributes.side_margin
        #self.side_margin = self.__DEFAULT_SIDE_MARGIN
        
        self.top_margin = self.section_style.section_attributes.top_margin
        #self.top_margin = self.__DEFAULT_TOP_MARGIN
        

        self.bullet_point = bullet_point
        #if bullet_point:self.bullet_point = bullet_point
        
        self.height_buffer = self.section_style.section_attributes.height_buffer
        #if height_buffer:self.height_buffer = height_buffer
        if self.bullet_point:
            self.info_list, self.attribute_weight_list = self.parse_bullet()
        else:
            self.info_list, self.attribute_weight_list = self.parse_regular()

        self.wrap_forgive = self.section_style.section_attributes.wrap_forgive
        self.total_height, self.empty_height, self.sub_height_list = (
            self.get_height_section()
        )

    def parse_bullet(self) -> tuple[list[list], list[list]]:
        """
        returns the bullet point parsed version of all_info
        assign it to self.info_list in __init__
        """
        result_list = []
        attribute_list = []
        bull_0 = "• "
        if self.section_style.section_attributes.bullet_symbol is not None:
            bull_0 = self.section_style.section_attributes.bullet_symbol
        bull_1 = "<br/>"
        for row in self.raw_info_list:
            attribute_item_list = []
            skip_index = 0
            for i in range(len(row)):
                splitted_list = row[i].split()
                if len(splitted_list) > 0:
                    if splitted_list[0] == "/=-z+f]j":
                        skip_index = i + 1
                        curr_att = [splitted_list[1], int(splitted_list[2])]
                        attribute_item_list.append(curr_att)
                    else:
                        break
                else:
                    break
            attribute_list.append(attribute_item_list)

            curr_list = []
            curr_list.append(row[0 + skip_index])
            curr_list.append(row[1 + skip_index])
            content_str = ""
            for i in range(2 + skip_index, len(row)):
                curr_point = bull_0 + row[i] + bull_1
                content_str += curr_point
            curr_list.append(content_str)
            result_list.append(curr_list)
        return result_list, attribute_list

    def parse_regular(self):
        """
        returns the bullet point parsed version of all_info
        assign it to self.info_list in __init__
        """
        result_list = []
        attribute_list = []
        for row in self.raw_info_list:
            attribute_item_list = []
            skip_index = 0
            for i in range(len(row)):
                splitted_list = row[i].split()
                if len(splitted_list) > 0:
                    if splitted_list[0] == "/=-z+f]j":
                        skip_index = i + 1
                        curr_att = [splitted_list[1], int(splitted_list[2])]
                        attribute_item_list.append(curr_att)
                    else:
                        break
                else:
                    break
            attribute_list.append(attribute_item_list)
            curr_list = []
            curr_list.append(row[0 + skip_index])
            curr_list.append(row[1 + skip_index])
            curr_list.append(row[2 + skip_index])
            result_list.append(curr_list)
        return result_list, attribute_list

    def add_info(self, new_info: list[3]) -> None:
        """
        add a subsection in the form of a list onto the info list
        """
        self.info_list.append(new_info)

    def display_info(self) -> None:
        """
        show the information in the section to the console
        """
        for information in self.info_list:
            print("Title: " + information[0] + ";   " + information[1])
            print("Info: " + information[2] + "\n")

    def get_height_subsection_index(self, sec_index: int) -> int:
        """
        Get the height of a subsection
        Reference by its index
        """
        subsection = self.info_list[sec_index]
        total_h = 0
        # subsection title, MUST BE one line:
        total_h += self.font_subright_style.font_attributes.leading
        total_h += self.font_subtitle_style.font_attributes.space_before
        # content: handle both paragraph and bullet points

        if self.bullet_point:
            line_width = A4[0] - 2 * self.side_margin - self.wrap_forgive - 20
            num_of_len = 0
            content_start = 0
            for n in range(len(self.raw_info_list[sec_index])):
                splitted_list = self.raw_info_list[sec_index][n].split()
                if len(splitted_list) > 0:
                    if splitted_list[0] == "/=-z+f]j":
                        content_start += 1
                    else:
                        break
                else:
                    break
            for i in range(2 + content_start, len(self.raw_info_list[sec_index])):
                point_len = stringWidth(
                    self.raw_info_list[sec_index][i],
                    self.font_text.fontName,
                    self.font_text.fontSize,
                )
                num_of_len += math.ceil(point_len / line_width)
            total_h += num_of_len * self.font_text.leading
        else:
            total_width = stringWidth(
                subsection[2], self.font_text.fontName, self.font_text.fontSize
            )
            line_width = A4[0] - 2 * self.side_margin - self.wrap_forgive
            num_of_lines = (total_width // line_width) + 1
            sub_text_height = num_of_lines * self.font_text.leading
            total_h += sub_text_height
            total_h += self.font_subtitle_style.font_attributes.space_before
        return total_h

    def get_height_subsection_list(self, sec_list: list) -> int:
        """
        Get the height of a subsection
        the subsection is taken in as input
        """
        subsection = sec_list
        total_h = 0
        # subsection title, MUST BE one line:
        total_h += self.font_subright_style.font_attributes.leading
        total_h += self.font_subtitle_style.font_attributes.space_before
        # content: handle both paragraph and bullet points
        if self.bullet_point:
            line_width = A4[0] - 2 * self.side_margin - self.wrap_forgive - 25
            num_of_len = 0
            content_start = 0
            for n in range(len(sec_list)):
                splitted_list = sec_list[n].split()
                if len(splitted_list) > 0:
                    if splitted_list[0] == "/=-z+f]j":
                        content_start += 1
                    else:
                        break
                else:
                    break
            for i in range(2 + content_start, len(sec_list)):
                point_len = stringWidth(
                    sec_list[i], self.font_text.fontName, self.font_text.fontSize
                )
                num_of_len += math.ceil(point_len / line_width)
            total_h += num_of_len * self.font_text.leading
        else:
            total_width = stringWidth(
                subsection[2], self.font_text.fontName, self.font_text.fontSize
            )
            line_width = A4[0] - 2 * self.side_margin - self.wrap_forgive
            num_of_lines = (total_width // line_width) + 1
            sub_text_height = num_of_lines * self.font_text.leading
            total_h += sub_text_height
        total_h += self.font_subtitle_style.font_attributes.space_before
        return total_h

    def get_height_section(self) -> tuple[int, int, list]:
        """
        Find the proper height on the doc for the entire section
        Assume A4 size paper
        Also gets the height list of each subsection
        """
        total_height = 0
        empty_height = (
            self.height_buffer + self.top_margin + self.font_title_style.font_attributes.font_size
        )
        total_height += self.height_buffer
        total_height += self.top_margin
        sub_hlist = []
        # section title:
        total_height += self.font_title_style.font_attributes.font_size
        if self.bullet_point:
            for subsection in self.raw_info_list:
                total_height += self.get_height_subsection_list(subsection)
                sub_hlist.append(self.get_height_subsection_list(subsection))
        else:
            for subsection in self.info_list:
                total_height += self.get_height_subsection_list(subsection)
                sub_hlist.append(self.get_height_subsection_list(subsection))
        return total_height, empty_height, sub_hlist
