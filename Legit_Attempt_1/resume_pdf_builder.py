from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Frame, Paragraph, KeepInFrame, Spacer
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import standard_section
import resume_info
import fonts


# Parameters:
#######################################
pdf_name = "Resume11.pdf"
side_margin = 25
#######################################


def build_all_frames(frame_heights: list[int], margin: int) -> list:
    result = []
    total_height = -1
    for frame_h in frame_heights:
        total_height += frame_h
        new_frame = Frame(-1, A4[1] - total_height, A4[0]+2, 
                          frame_h, leftPadding=side_margin+1, 
                          rightPadding=side_margin+1, showBoundary=True)
        result.append(new_frame)
    return result


def build_skills(skills_info: resume_info.AuxSectionsInfo) -> list:
    """
    Builds the content list for a section that uses skills format
    """
    section_content = []
    section_title_1 = Paragraph(skills_info.title, all_fonts.section_title)
    section_content.append(section_title_1)
    skill_items = skills_info.skills_list
    counter = 0
    while counter < (len(skill_items)-1):
        content_1 = Paragraph(skill_items[counter], all_fonts.point_left)
        counter += 1
        content_2 = Paragraph(skill_items[counter], all_fonts.point_right)
        section_content.append(content_1)
        section_content.append(content_2)
        counter += 1
    if counter < len(skill_items):
        content_1 = Paragraph(skill_items[counter], all_fonts.point_left)
        section_content.append(content_1)
    return section_content


def build_standard_content_section(standard_sec) -> list: 
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


styles = getSampleStyleSheet()

# Prepare a canvas object
c = canvas.Canvas(pdf_name, pagesize=A4)
c.setLineWidth(0.3)

resume_informations = resume_info.ResumeInfo()
all_fonts = fonts.AllFonts()

frames = build_all_frames(resume_informations.height_list, side_margin)

all_contents = []

header_container = resume_informations.heading_info

# Two paragraphs for the header
custom_space = Spacer(width=0, height=header_container.top_space)
title_text = Paragraph(header_container.title, all_fonts.name_font)
basic_info_text = Paragraph(header_container.header_basic_info,
                            all_fonts.personal_info_font)

# Add to this array in order to populate the title
header_content = [custom_space, title_text, basic_info_text]
all_contents.append(header_content)

all_contents.append(build_skills(resume_informations.skills_info))
# Info in the box
all_contents.append(build_standard_content_section(
    resume_informations.edu_info))
all_contents.append(build_standard_content_section(
    resume_informations.exp_info))
all_contents.append(build_standard_content_section(
    resume_informations.proj_info))


# Add content to frames using canvas
frames[0].addFromList(all_contents[0], c)
frames[1].addFromList(all_contents[1], c)
frames[2].addFromList(all_contents[2], c)
frames[3].addFromList(all_contents[3], c)
frames[4].addFromList(all_contents[4], c)

c.save()
print("all done!")
