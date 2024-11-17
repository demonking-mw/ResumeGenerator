from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.pdfgen import canvas
import os
from . import resume_info
from . import fonts

class ResumeBuilder:
    '''
    The class that builds the resume
    Calling workflow: 
    b = ResumeBuilder(...)
    b.build()
    '''
    def build_all_frames(self, frame_heights: list[int]) -> list:
        '''
        Builds the lists required for making the resume from each data file
        '''
        result = []
        total_height = -1
        for frame_h in frame_heights:
            total_height += frame_h
            new_frame = Frame(-1, A4[1] - total_height, A4[0]+2,
                            frame_h, leftPadding=self.side_margin+1,
                            rightPadding=self.side_margin+1, showBoundary=True)
            result.append(new_frame)
        return result

    def build_skills(self, skills_info: resume_info.AuxSectionsInfo) -> list:
        """
        Builds the content list for a section that uses skills format
        """
        section_content = []
        section_title_1 = Paragraph(skills_info.title, self.all_fonts.section_title)
        section_content.append(section_title_1)
        skill_items = skills_info.skills_list
        counter = 0
        while counter < (len(skill_items) - 1):
            content_1 = Paragraph(skill_items[counter], self.all_fonts.point_left)
            counter += 1
            content_2 = Paragraph(skill_items[counter], self.all_fonts.point_right)
            section_content.append(content_1)
            section_content.append(content_2)
            counter += 1
        if counter < len(skill_items):
            content_1 = Paragraph(skill_items[counter], self.all_fonts.point_left)
            section_content.append(content_1)
        return section_content

    def build_standard_content_section(self, standard_sec) -> list:
        """
        Builds the content list for a section that uses standard format
        Here: each element of content is [title, date, description]
        """
        section_content = []
        section_title_1 = Paragraph(standard_sec.title, standard_sec.font_title)
        section_content.append(section_title_1)
        for content in standard_sec.info_list:
            content_title_1 = Paragraph(content[0], standard_sec.font_subtitle)
            content_title_2 = Paragraph(content[1], standard_sec.font_subright)
            content_para = Paragraph(content[2], standard_sec.font_text)
            section_content.append(content_title_1)
            section_content.append(content_title_2)
            section_content.append(content_para)
        return section_content

    def build(self) -> None:
        '''
        builds the pdf
        '''
        # Make the file path
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf_path = os.path.join(downloads_folder, pdf_name)
        # Prepare a canvas object
        c = canvas.Canvas(pdf_path, pagesize=A4)
        c.setLineWidth(0.3)

        frames = self.build_all_frames(
            self.resume_informations.height_list)

        all_contents = []

        header_container = self.resume_informations.heading_info

        # Two paragraphs for the header
        custom_space = Spacer(width=0, height=header_container.top_space)
        title_text = Paragraph(header_container.title, self.all_fonts.name_font)
        basic_info_text = Paragraph(
            header_container.header_basic_info, self.all_fonts.personal_info_font
        )

        # Add to this array in order to populate the title
        header_content = [custom_space, title_text, basic_info_text]
        all_contents.append(header_content)

        all_contents.append(self.build_skills(self.resume_informations.skills_info))
        # Info in the box
        all_contents.append(
            self.build_standard_content_section(self.resume_informations.edu_info)
        )
        all_contents.append(
            self.build_standard_content_section(self.resume_informations.exp_info)
        )
        all_contents.append(
            self.build_standard_content_section(self.resume_informations.proj_info)
        )

        # Add content to frames using canvas
        frames[0].addFromList(all_contents[0], c)
        frames[1].addFromList(all_contents[1], c)
        frames[2].addFromList(all_contents[2], c)
        frames[3].addFromList(all_contents[3], c)
        frames[4].addFromList(all_contents[4], c)

        c.save()
        print("all done!")

    def __init__(
        self,
        target_pdf_name: str,
        overall_side_margin: int,
        info_folder: str,
        gpt_model: str = "gpt-4o-mini",
    ) -> None:
        self.pdf_name = target_pdf_name
        self.side_margin = overall_side_margin
        self.resume_informations = resume_info.ResumeInfo(info_folder, gpt_model)
        self.all_fonts = fonts.AllFonts()


# Parameters:
#######################################
pdf_name = "BobSmithResume1.pdf"
side_margin = 25
r = ResumeBuilder(pdf_name, side_margin, "Accurate")
r.build()
#######################################
