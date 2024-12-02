from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QTextEdit,
)
import os
from PyQt6.QtCore import Qt
from ...FileGenerator import resume_pdf_builder


class Generate(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.model_list = ["gpt-4o", "gpt-4o-mini"]
        self.folder_list = self.get_folders()
        self.model_sel = "gpt-4o-mini"
        self.folder_sel = self.folder_list[0]
        # self.job_desc = ""
        # self.job_resp = ""
        # self.job_req = ""
        self.header_label = QLabel("Resume Generator")
        self.header_label.setFixedHeight(40)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setStyleSheet("font-weight: bold; font-size: 15px;")
        self.layout.addWidget(self.header_label)

        self.folder_section = QHBoxLayout()
        self.folder_header = QLabel("Select folder:")
        self.folder_options = QComboBox()
        self.folder_options.addItems(self.folder_list)
        self.folder_options.currentIndexChanged.connect(self.folder_selected)
        self.folder_options.setCurrentIndex(0)
        self.folder_section.addWidget(self.folder_header)
        self.folder_section.addWidget(self.folder_options)
        self.layout.addLayout(self.folder_section)

        self.model_section = QHBoxLayout()
        self.model_header = QLabel("Select model:")
        self.model_options = QComboBox()
        self.model_options.addItems(self.model_list)
        self.model_options.currentIndexChanged.connect(self.item_selected)
        self.model_options.setCurrentIndex(1)
        self.model_section.addWidget(self.model_header)
        self.model_section.addWidget(self.model_options)
        self.layout.addLayout(self.model_section)

        self.f_sec = QVBoxLayout()
        self.f_header = QLabel("Enter output filename")
        self.f_input = QLineEdit()
        self.f_input.setPlaceholderText("grass_allergy")
        self.f_sec.addWidget(self.f_header)
        self.f_sec.addWidget(self.f_input)
        self.layout.addLayout(self.f_sec)

        # Set up a QStackedWidget to hold the pages
        self.stack = QStackedWidget()

        self.complete_widget = QWidget()
        self.complete_layout = QVBoxLayout()

        self.desc_sec = QVBoxLayout()
        self.desc_header = QLabel("Enter Job Description")
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Developing grass allergy relief pills ...")
        self.desc_sec.addWidget(self.desc_header)
        self.desc_sec.addWidget(self.desc_input)
        self.complete_layout.addLayout(self.desc_sec)

        self.resp_sec = QVBoxLayout()
        self.resp_header = QLabel("Enter Job Responsibility")
        self.resp_input = QTextEdit()
        self.resp_input.setPlaceholderText("Touch grass on a daily basis ...")
        self.resp_sec.addWidget(self.resp_header)
        self.resp_sec.addWidget(self.resp_input)
        self.complete_layout.addLayout(self.resp_sec)

        self.req_sec = QVBoxLayout()
        self.req_header = QLabel("Enter Job Requirement")
        self.req_input = QTextEdit()
        self.req_input.setPlaceholderText("Have grass allergy ...")
        self.req_sec.addWidget(self.req_header)
        self.req_sec.addWidget(self.req_input)
        self.complete_layout.addLayout(self.req_sec)

        self.direct_widget = QWidget()
        self.direct_layout = QVBoxLayout()

        self.paste_sec = QVBoxLayout()
        self.paste_header = QLabel("Paste 'em all here")
        self.paste_input = QTextEdit()
        self.paste_input.setPlaceholderText("Grass is green, touch it ...")
        self.paste_sec.addWidget(self.paste_header)
        self.paste_sec.addWidget(self.paste_input)
        self.direct_layout.addLayout(self.paste_sec)

        self.direct_widget.setLayout(self.direct_layout)
        self.complete_widget.setLayout(self.complete_layout)

        self.stack.addWidget(self.complete_widget)
        self.stack.addWidget(self.direct_widget)

        button_cont = QWidget(self)
        button_layout = QHBoxLayout()
        sel_buttons = [
            ("Individual Insertion", 0),
            ("One Paste", 1),
        ]
        for label, index in sel_buttons:
            sel_button = QPushButton(label)
            sel_button.setStyleSheet(
                """
            QPushButton {
                background-color: white; /* Background color */
                border: 1px solid black; /* Border style */
                border-radius: 5px; /* Rounded corners */
                color: black; /* Text color */
                font-size: 10px; /* Font size */
                padding: 2px; /* Padding inside the button */
            }
            QPushButton:hover {
                background-color: skyblue; /* Background color on hover */
            }
            QPushButton:pressed {
                background-color: dodgerblue; /* Background color when pressed */
                color: white; /* Text color when pressed */
            }
        """
            )
            sel_button.clicked.connect(lambda _, idx=index: self.switch_page(idx))
            button_layout.addWidget(sel_button)
        button_cont.setLayout(button_layout)

        self.conf_button = QPushButton("CONFIRM AND GENERATE")
        self.gen_status = QLabel("")
        self.gen_status.setWordWrap(True)
        self.conf_button.clicked.connect(self.on_confirm)

        self.layout.addWidget(self.stack)
        self.layout.addWidget(button_cont)
        self.layout.addWidget(self.conf_button)
        self.layout.addWidget(self.gen_status)

        self.setLayout(self.layout)

    def item_selected(self, index) -> str:
        # Get the selected item and display it on the label
        selected_item = self.model_list[index]
        self.model_sel = selected_item

    def folder_selected(self, index) -> str:
        selected_item = self.folder_list[index]
        self.folder_sel = selected_item

    def get_folders(self):
        rel_path = "ResumeGenerator/Informations/"
        abs_file_path = os.path.abspath(rel_path)
        folder_names = [
            name
            for name in os.listdir(abs_file_path)
            if os.path.isdir(os.path.join(abs_file_path, name))
        ]
        return folder_names

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        if index == 0:
            self.paste_input.clear()
        else:
            self.desc_input.clear()
            self.resp_input.clear()
            self.req_input.clear()

    def on_confirm(self):
        resp = self.resp_input.toPlainText()
        req = self.req_input.toPlainText()
        desc = self.desc_input.toPlainText()
        f_name = self.f_input.text()
        paste_info = self.paste_input.toPlainText()
        if self.folder_sel != "":
            if resp != "" and req != "" and desc != "":
                self.gen_status.setText("Build commenced")
                try:
                    self.conf_button.setEnabled(False)
                    pdf_name = f_name + ".pdf"
                    side_margin = 25
                    r = resume_pdf_builder.ResumeBuilder(
                        pdf_name,
                        side_margin,
                        self.folder_sel,
                        desc,
                        resp,
                        req,
                        gpt_model=self.model_sel,
                    )
                    r.build()
                    self.gen_status.setText("Build success, resume downloaded")
                    self.conf_button.setEnabled(True)
                    self.desc_input.clear()
                    self.resp_input.clear()
                    self.req_input.clear()
                except Exception as error:
                    self.gen_status.setText(str(error))
                    self.conf_button.setEnabled(True)
            elif paste_info != "":
                self.gen_status.setText("Build commenced")
                try:
                    self.conf_button.setEnabled(False)
                    pdf_name = f_name + ".pdf"
                    side_margin = 25
                    r = resume_pdf_builder.ResumeBuilder(
                        pdf_name,
                        side_margin,
                        self.folder_sel,
                        desc,
                        resp,
                        req,
                        all_job_info=paste_info,
                        gpt_model=self.model_sel,
                    )
                    r.build()
                    self.gen_status.setText("Build success, resume downloaded")
                    self.conf_button.setEnabled(True)
                    self.paste_input.clear()
                except Exception as error:
                    self.gen_status.setText(str(error))
                    self.conf_button.setEnabled(True)
            else:
                self.gen_status.setText("Missing Info!!")
        else:
            self.gen_status.setText("Missing Info!!")
