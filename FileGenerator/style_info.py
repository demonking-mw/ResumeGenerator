'''
A style class that stores enough information for both paragraph style and font. Make a function that returns a ParagraphStyle object for report lab, as well as functions to return specific info for other presets. Helps latex transfer.
Requires:
 
for font:
- name
- fontName
- fontSize
- textColor
- alignment
- spaceBefore
- spaceAfter
- leading

for section:
- side margin
- top margin
- height buffer
- wrap forgive
- bullet point
- bullet symbol
- paper width

others:
- dictionary of remaining attributes
- dictionary of all fonts
'''
import dataclasses
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

@dataclasses.dataclass
class FontAttributes:
    name: str = None
    font_name: str = None
    font_size: int = None
    text_color_hex: str = None # hex color
    alignment: int = None
    space_before: int = None
    space_after: int = None
    leading: int = None

@dataclasses.dataclass
@dataclasses.dataclass
class SectionAttributes:
    side_margin: int = None
    top_margin: int = None
    height_buffer: int = None
    wrap_forgive: int = None
    bullet_point: bool = None
    bullet_symbol: str = None
    paper_width: int = None

class StyleInfo:
    """
    A class that stores all custom fonts/paragraph styles 
    """
    def __init__(self, font_attributes: FontAttributes=None, section_attributes: SectionAttributes=None, other_attributes: dict[str, any]=None, subStyleInfo: dict[str, 'StyleInfo']=None) -> None:
        self.font_attributes = font_attributes
        self.section_attributes = section_attributes
        self.other_attributes = other_attributes
        self.subsections = subStyleInfo

    def get_paragraph_style(self) -> ParagraphStyle:
        '''
        returns a ParagraphStyle object for report lab
        '''
        if not self.font_attributes:
            raise ValueError("Font attributes are not set")
        return ParagraphStyle(
            name=self.font_attributes.name,
            fontName=self.font_attributes.font_name,
            fontSize=self.font_attributes.font_size,
            textColor=colors.HexColor(self.font_attributes.text_color_hex) if self.font_attributes.text_color_hex else colors.black,
            alignment=self.font_attributes.alignment,
            spaceBefore=self.font_attributes.space_before,
            spaceAfter=self.font_attributes.space_after,
            leading=self.font_attributes.leading,
        )
    
    