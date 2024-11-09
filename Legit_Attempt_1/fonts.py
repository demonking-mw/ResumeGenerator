"""
A class that stores all custom fonts 
"""

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


class AllFonts:
    """
    Stores all font info
    """
    section_title = ParagraphStyle(
                                name="SectTitleFont",
                                fontName='Times-Bold',
                                fontSize=14,
                                textColor=colors.black,
                                alignment=1,
                                spaceAfter=0,
                                leading=12)
    subsection_title = ParagraphStyle(
                                name="SectTitleFont",
                                fontName='Times-Roman',
                                fontSize=13,
                                textColor=colors.black,
                                spaceBefore=8,
                                alignment=0, spaceAfter=0,
                                leading=0)
    subright_title = ParagraphStyle(
                                name="SectTitleFont",
                                fontName='Times-Roman',
                                fontSize=13,
                                textColor=colors.black,
                                alignment=2,
                                spaceAfter=0,
                                leading=15)
    text_font_standard_sec = ParagraphStyle(
                                name="paraFont",
                                fontName='Times-Roman',
                                fontSize=11,
                                textColor=colors.black,
                                alignment=0,
                                spaceAfter=0,
                                leading=12)
    name_font = ParagraphStyle(
                                name="nameFont",
                                fontName='Helvetica-Bold',
                                fontSize=16,
                                textColor=colors.black,
                                alignment=1,
                                spaceAfter=3,
                                leading=18)

    personal_info_font = ParagraphStyle(
                                name="personalInfoFont",
                                fontName='Times-Bold',
                                fontSize=12,
                                textColor=colors.black,
                                alignment=1,
                                spaceAfter=0,
                                leading=15
    )
    point_left = ParagraphStyle(
                                name="SectTitleFont",
                                fontName='Times-Roman',
                                fontSize=11,
                                textColor=colors.black,
                                spaceBefore=0,
                                alignment=0, spaceAfter=0,
                                leading=0)
    point_right = ParagraphStyle(
                                name="SectTitleFont",
                                fontName='Times-Roman',
                                fontSize=11,
                                textColor=colors.black,
                                leftIndent=A4[0]/2,
                                alignment=0,
                                spaceAfter=0,
                                leading=12)

    def __init__(self) -> None:
        print("fonts init")
