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
        self.target_folder = ""
        self.target_file = ""
        self.file_display_text = ""
        self.file_display_simple = ""
        self.file_as_list = []
        self.item_title_list = []
        self.target_item = ""
        self.target_index = 0

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

        # Set and display
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

    def display_widget(self):
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

    def operation_widget(self):
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
        self.setStyleSheet("QWidget#operation_button_widget { border: 1px solid black; }")
        self.operation_button_widget.setObjectName("operation_button_widget")
        self.operation_button_layout.addStretch()

        self.add_button = QPushButton("Add in front")
        self.operation_button_layout.addWidget(self.add_button)

        self.modify_button = QPushButton("Modify")
        self.operation_button_layout.addWidget(self.modify_button)

        self.delete_button = QPushButton("Delete")
        self.operation_button_layout.addWidget(self.delete_button)

        self.operation_button_layout.addStretch()
        self.operation_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.operation_button_widget.setLayout(self.operation_button_layout)
        self.operation_layout.addWidget(self.operation_button_widget)

        # Add
        self.operation_widget.setLayout(self.operation_layout)

    def build_item(self):
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
        self.build_item_widget.setFixedHeight(200)
        self.build_item_layout = QVBoxLayout()

        # Add time
        self.add_time_layout = QHBoxLayout()
        self.time_prompt = QLabel("Add time:")
        self.time_input = QLineEdit()
        self.add_time_layout.addWidget(self.time_prompt)
        self.add_time_layout.addWidget(self.time_input)
        self.build_item_layout.addLayout(self.add_time_layout)

        # Add descriptions
        self.desc_layout = QVBoxLayout()
        self.desc_prompt = QLabel("Add descriptions, itemize by newline, wrap with quotation if , included:")
        self.desc_input = QTextEdit()
        self.desc_layout.addWidget(self.desc_prompt)
        self.desc_layout.addWidget(self.desc_input)
        self.build_item_layout.addLayout(self.desc_layout)

        # Add attributes
        self.att_layout = QVBoxLayout()
        self.att_title_layout = QHBoxLayout()
        self.att_prompt = QLabel("Add attributes, format is ALL_CAP, separate each with newline:")
        self.add_arrow_button = QPushButton("attribute->score")
        self.att_input = QTextEdit()
        self.add_arrow_button.clicked.connect(self.add_arrow)
        
        self.att_title_layout.addWidget(self.att_prompt)
        self.att_title_layout.addWidget(self.add_arrow_button)
        self.att_layout.addLayout(self.att_title_layout)
        self.att_layout.addWidget(self.att_input)
        self.build_item_layout.addLayout(self.att_layout)

        # Add
        self.build_item_widget.setLayout(self.build_item_layout)

    def add_arrow(self):
        cursor = self.att_input.textCursor()
        cursor.insertText("----->")

    def info_selected(self, index):
        if index <= 0:
            self.target_item = ""
            self.add_button.setText("Add to front")
            self.target_index = 0
        else:
            self.target_item = self.file_as_list[index - 1]
            self.add_button.setText("Add After Selected")
            self.target_index = index-1

    def communicate(self, target_folder, target_file, ObtainInfo):

        self.target_folder = target_folder
        self.target_file = target_file
        self.ObtainInfo = ObtainInfo
        self.info_update()

    def info_update(self):
        self.file_display_text, self.file_display_simple, self.file_as_list, self.item_title_list = self.ObtainInfo(
            self.target_folder, self.target_file
        )
        self.file_as_text.setPlainText(self.file_display_simple)
        self.info_selector.clear()
        self.info_selector.addItem("SELECT ITEM")
        self.info_selector.addItems(self.item_title_list)
