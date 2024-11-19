from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit, QPushButton

from ...FileGenerator import resume_pdf_builder

class Generate(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.model_list = ["gpt-4o", "gpt-4o-mini"]
        self.model_sel = "gpt-4o-mini"
        # self.job_desc = ""
        # self.job_resp = ""
        # self.job_req = ""
        self.header_label = QLabel("Resume Generator")
        self.header_label.setFixedSize(200, 40)
        self.layout.addWidget(self.header_label)

        self.model_section = QHBoxLayout()
        self.model_header = QLabel("Select model:")
        self.model_options = QComboBox()
        self.model_options.addItems(self.model_list)
        self.model_options.currentIndexChanged.connect(self.item_selected)
        self.model_section.addWidget(self.model_header)
        self.model_section.addWidget(self.model_options)
        self.layout.addLayout(self.model_section)

        self.f_sec = QVBoxLayout()
        self.f_header = QLabel("Enter target filename")
        self.f_input = QLineEdit()
        self.f_input.setPlaceholderText("grass_allergy")
        self.f_sec.addWidget(self.f_header)
        self.f_sec.addWidget(self.f_input)
        self.layout.addLayout(self.f_sec)

        self.desc_sec = QVBoxLayout()
        self.desc_header = QLabel("Enter Job Description")
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Developing grass allergy relief pills ...")
        self.desc_sec.addWidget(self.desc_header)
        self.desc_sec.addWidget(self.desc_input)
        self.layout.addLayout(self.desc_sec)

        self.resp_sec = QVBoxLayout()
        self.resp_header = QLabel("Enter Job Responsibility")
        self.resp_input = QLineEdit()
        self.resp_input.setPlaceholderText("Touch grass on a daily basis ...")
        self.resp_sec.addWidget(self.resp_header)
        self.resp_sec.addWidget(self.resp_input)
        self.layout.addLayout(self.resp_sec)

        self.req_sec = QVBoxLayout()
        self.req_header = QLabel("Enter Job Requirement")
        self.req_input = QLineEdit()
        self.req_input.setPlaceholderText("Have grass allergy ...")
        self.req_sec.addWidget(self.req_header)
        self.req_sec.addWidget(self.req_input)
        self.layout.addLayout(self.req_sec)

        self.conf_button = QPushButton("CONFIRM AND GENERATE")
        self.gen_status = QLabel()
        self.conf_button.clicked.connect(self.on_confirm)
        self.layout.addWidget(self.conf_button)
        self.layout.addWidget(self.gen_status)

        self.setLayout(self.layout)

    def item_selected(self, index) -> str:
        # Get the selected item and display it on the label
        selected_item = self.model_list[index]
        self.model_sel = selected_item
        print(selected_item)

    def on_confirm(self):
        resp = self.resp_input.text()
        req = self.req_input.text()
        desc = self.desc_input.text()
        f_name = self.f_input.text()
        if resp != "" and req != "" and desc != "":
            try:

                print("start")
                pdf_name = f_name + ".pdf"
                side_margin = 25
                r = resume_pdf_builder.ResumeBuilder(pdf_name, side_margin, "Accurate", desc, resp, req, gpt_model=self.model_sel)
                r.build()
                self.gen_status.setText("Build success, resume downloaded")
            except Exception as error:
                self.gen_status.setText("Build failed, error: " + error)
        else:
            self.gen_status.setText("Missing Info!!")
