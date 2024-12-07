from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QGridLayout,
    QTextEdit,
)
from PyQt6.QtCore import Qt

import os
from ...FileGenerator import file_parse
from . import view_info


class ModInfo(QWidget):

    def __init__(self, switch_page):

        super().__init__()
        self.layout = QVBoxLayout()

        # Functions
        self.switch_page = switch_page

        # Information
        self.set_info_variables()

        # Header
        self.header_label = QLabel("Information Modifier")
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-weight: bold; font-size: 15px;")
        self.header_label.setFixedHeight(20)
        self.layout.addWidget(self.header_label)

        # Display
        self.display_widget()
        self.layout.addWidget(self.info_display_widget)

        # Operation
        self.operation_widget()
        self.layout.addWidget(self.operation_widget)

        # Build item
        self.build_item()
        self.layout.addWidget(self.build_item_widget)

        # Status display
        self.stat_display = QLabel()
        self.layout.addWidget(self.stat_display)

        # Back to view
        self.back_button = QPushButton("VIEW_INFO")
        self.back_button.clicked.connect(self.return_to_view)
        self.layout.addWidget(self.back_button)

        # Set and display
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

    def set_info_variables(self) -> None:
        '''
        make __init__ cleaner
        use the fold view option to have a better time looking at this shit
        '''
        self.target_folder = ""
        self.target_file = ""
        self.file_display_text = ""
        self.file_display_simple = ""
        self.file_as_list = []
        self.item_title_list = []
        self.target_item = ""
        self.target_index = -1 # -1 for no selection

    def clear_fields(self) -> None:
        '''
        clear the inputs
        '''
        self.title_input.clear()
        self.time_input.clear()
        self.desc_input.clear()
        self.att_input.clear()

    def return_to_view(self) -> None:
        '''
        returns to the view_info page
        clears input fields
        '''
        self.set_info_variables()
        self.clear_fields()
        self.switch_page(0)

    def display_widget(self)  -> None:
        # Displayer: shows everything in the file
        self.info_display_widget = QWidget()
        self.info_display_widget.setFixedHeight(150)
        self.info_display = QVBoxLayout()
        # Heading
        self.info_display_heading = QLabel("Section Selected:")
        self.info_display.addWidget(self.info_display_heading)
        # File display in text
        self.file_as_text = QTextEdit()
        self.file_as_text.setReadOnly(True)
        self.info_display.addWidget(self.file_as_text)
        self.info_display_widget.setLayout(self.info_display)

    def operation_widget(self) -> None:
        # Selector
        self.operation_widget = QWidget()
        self.operation_widget.setFixedHeight(100)
        self.operation_layout = QVBoxLayout()
        self.operation_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Info selector dropdowns and prompt
        self.info_selector_widget = QWidget()
        self.info_selector_widget.setFixedHeight(40)
        self.info_selector_layout = QHBoxLayout()

        self.info_sel_prompt = QLabel("Select item to modify:")
        self.info_selector_layout.addWidget(self.info_sel_prompt)

        self.info_selector = QComboBox()
        self.info_selector.addItem("SELECT ITEM")
        self.info_selector.addItems(self.item_title_list)
        self.info_selector.setCurrentIndex(0)
        self.info_selector.currentIndexChanged.connect(self.info_selected)
        self.info_selector_layout.addWidget(self.info_selector)
        self.info_selector_widget.setLayout(self.info_selector_layout)
        self.operation_layout.addWidget(self.info_selector_widget)

        # Option buttons: add mod del
        self.operation_button_widget = QWidget()
        self.operation_button_widget.setFixedHeight(40)
        self.operation_button_layout = QHBoxLayout()
        self.setStyleSheet(
            "QWidget#operation_button_widget { border: 1px solid black; }"
        )
        self.operation_button_widget.setObjectName("operation_button_widget")
        self.operation_button_layout.addStretch()

        self.add_button = QPushButton("Add in front")
        self.add_button.clicked.connect(self.add_item_on_click)
        self.operation_button_layout.addWidget(self.add_button)

        self.modify_button = QPushButton("Modify")
        self.modify_button.clicked.connect(lambda: self.change_item(1))
        self.operation_button_layout.addWidget(self.modify_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_item)
        self.operation_button_layout.addWidget(self.delete_button)

        self.operation_button_layout.addStretch()
        self.operation_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.operation_button_widget.setLayout(self.operation_button_layout)
        self.operation_layout.addWidget(self.operation_button_widget)

        # Add
        self.operation_widget.setLayout(self.operation_layout)

    def build_item(self) -> None:
        """
        Collect the following from the user:
        attribute_list: list[list],
        folder_name: str, #already have
        file_name: str, #already have
        header: str, #already have
        time: str,
        descriptions: list,
        location: int = 0,
        """
        self.build_item_widget = QWidget()
        self.build_item_widget.setStyleSheet("background-color: lightgray;")
        self.build_item_widget.setFixedHeight(250)
        self.build_item_layout = QVBoxLayout()

        # Add title
        self.add_title_layout = QHBoxLayout()
        self.title_prompt = QLabel("Enter title or name for heading:")
        self.title_input = QLineEdit()
        self.title_input.setStyleSheet("background-color: white;")
        self.add_title_layout.addWidget(self.title_prompt)
        self.add_title_layout.addWidget(self.title_input)
        self.build_item_layout.addLayout(self.add_title_layout)

        # Add time
        self.add_time_layout = QHBoxLayout()
        self.time_prompt = QLabel("Enter time:")
        self.time_input = QLineEdit()
        self.time_input.setStyleSheet("background-color: white;")
        self.add_time_layout.addWidget(self.time_prompt)
        self.add_time_layout.addWidget(self.time_input)
        self.build_item_layout.addLayout(self.add_time_layout)

        # Add descriptions
        self.desc_layout = QVBoxLayout()
        self.desc_prompt = QLabel(
            "Add descriptions or sub-traits for skills, itemize by newline, wrap with quotation if , included:"
        )
        self.desc_input = QTextEdit()
        self.desc_input.setStyleSheet("background-color: white;")
        self.desc_layout.addWidget(self.desc_prompt)
        self.desc_layout.addWidget(self.desc_input)
        self.build_item_layout.addLayout(self.desc_layout)

        # Add attributes
        self.att_layout = QVBoxLayout()
        self.att_title_layout = QHBoxLayout()
        self.att_prompt = QLabel(
            "Add attributes, format is ALL_CAP, separate each with newline:"
        )
        self.add_arrow_button = QPushButton("attribute->score")
        self.att_input = QTextEdit()
        self.att_input.setStyleSheet("background-color: white;")
        self.add_arrow_button.clicked.connect(self.add_arrow)

        self.att_title_layout.addWidget(self.att_prompt)
        self.att_title_layout.addWidget(self.add_arrow_button)
        self.att_layout.addLayout(self.att_title_layout)
        self.att_layout.addWidget(self.att_input)
        self.build_item_layout.addLayout(self.att_layout)

        # Add
        self.build_item_widget.setLayout(self.build_item_layout)

    def add_arrow(self) -> None:
        '''
        adds an arrow to the attribute input
        exact format as anticipated
        '''
        cursor = self.att_input.textCursor()
        cursor.insertText("----->")

    def info_selected(self, index: int) -> None:
        '''
        handle the selection of an item
        '''
        if index <= 0:
            self.target_item = ""
            self.add_button.setText("Add to front")
            self.target_index = -1
        else:
            self.target_item = self.item_title_list[index - 1]
            self.add_button.setText("Add After Selected")
            self.target_index = index - 1

    def communicate(self, target_folder: str, target_file: str, ObtainInfo) -> None:
        """
        Receiver of information from view_info
        saves the need of running file parse again on start
        ObtainInfo is a function to obtain info given by view_info
        
        def ObtainInfo(target_folder: str, target_file: str) -> 
        tuple[str, str, list[str], list[str]]
        """
        self.target_folder = target_folder
        self.target_file = target_file
        self.ObtainInfo = ObtainInfo
        self.info_update()

    def change_item(self, mode: int) -> None:
        """
        mode=0 for add
        mode=1 for modify
        """
        name = self.title_input.text()
        inp_time = self.time_input.text()
        desc = self.desc_input.toPlainText().rstrip().split("\n")
        att = self.att_input.toPlainText().rstrip().split("\n")
        formatted_attributes = []
        att_format = True
        try:
            for at in att:
                if at == "":
                    continue
                attribute_list = at.split("----->")
                if len(attribute_list) != 2:
                    att_format = False
                formatted_attributes.append(attribute_list)
        except Exception as e:
            att_format = False

        if self.target_file == "HEADING.csv":
            self.stat_display.setText(
                "Header modified using only the first line of description, attributes not used"
            )
            try:
                fp = file_parse.FileAccMod()
                if len(desc) == 0:
                    fp.change_header(self.target_folder, name, "")
                else:
                    fp.change_header(self.target_folder, name, desc[0])
                self.clear_fields()
            except Exception as e:
                self.stat_display.setText("Mod header error ->"+ str(e))
        else:
            if not att_format:
                self.stat_display.setText("Attribute format error")
                return
            if self.target_file == "SKILLS.csv":
                if mode == 0:
                    fp = file_parse.FileAccMod()
                    fp.add_skill(desc, self.target_folder, name, self.target_index+1)
                    self.stat_display.setText(
                        "skills added with sub-traits from description"
                    )
                else:
                    self.stat_display.setText("delete the skill, then re-add with different value")

            else:
                # CHange standard section
                if mode == 0:
                    # add
                    self.stat_display.setText("Adding to standard section")
                    try:
                        fp = file_parse.FileAccMod()
                        fp.add_line_ss(
                            formatted_attributes,
                            self.target_folder,
                            self.target_file,
                            name,
                            inp_time,
                            desc,
                            self.target_index + 1,
                        )
                        self.clear_fields()
                    except Exception as e:
                        self.stat_display.setText("Add S.S error ->"+ str(e))
                else:
                    # mod
                    self.stat_display.setText("Modifying standard section")
                    try:
                        fp = file_parse.FileAccMod()
                        fp.mod_by_index_ss(
                            formatted_attributes,
                            self.target_folder,
                            self.target_file,
                            self.target_index+1, # True index including header
                            self.item_title_list[self.target_index],
                            inp_time,
                            desc,
                        )
                        self.clear_fields()
                    except Exception as e:
                        self.stat_display.setText("Mod S.S error ->"+ str(e))
        self.info_update()

    def delete_item(self) -> tuple[list, bool]:
        """
        deletes the item selected 
        using delete by index function from file_parse
        returns the item deleted as a list
        the bool is for success or failure
        """
        if self.target_index == -1:
            self.stat_display.setText("No item selected")
            self.info_update()
            return [], False

        try:
            fp = file_parse.FileAccMod()
            deleted_content = fp.del_by_index(self.target_folder, self.target_file, self.target_index)
            self.stat_display.setText("Delete success")
            self.info_update()
            return deleted_content, True
        except Exception as e:
            self.info_update()
            self.stat_display.setText("Delete error ->"+ str(e))

    def info_update(self) -> None:
        '''
        updates the information displayed
        '''
        (
            self.file_display_text,
            self.file_display_simple,
            self.file_as_list,
            self.item_title_list,
        ) = self.ObtainInfo(self.target_folder, self.target_file)
        self.file_as_text.setPlainText(self.file_display_simple)
        self.info_selector.clear()
        self.info_selector.addItem("SELECT ITEM")
        self.info_selector.addItems(self.item_title_list)

    def add_item_on_click(self) -> None:
        '''
        Handles onclick for add item button
        '''
        self.change_item(0)
        self.info_update()
