from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QGridLayout
)
import os
from ...FileGenerator import resume_pdf_builder


class ViewInfo(QWidget):
    def __init__(self):

        super().__init__()
        self.layout = QVBoxLayout()

        # Information
        self.target_folder_list = self.GetSub("ResumeGenerator/Informations")
        self.target_folder = ""
        self.target_file_list = []
        self.target_file = ""
        self.target_file_path = ""

        # Header
        self.header_label = QLabel("Information Viewer")
        self.header_label.setFixedSize(200, 40)
        self.layout.addWidget(self.header_label)

        # Selector
        self.selector_widget = QWidget()
        self.selector_widget.setFixedHeight(150)
        self.selector = QVBoxLayout()

        self.mod_button = QPushButton()
        self.mod_button.clicked.connect(self.ModFile)
        self.selector.addWidget(self.mod_button)

        self.info_selector_widget = QWidget()
        self.info_selector_widget.setFixedSize(300, 80)
        self.info_selector = self.InfoSelector()
        self.info_selector_widget.setLayout(self.info_selector)
        self.selector.addWidget(self.info_selector_widget)

        self.target_file_path_label = QLabel()
        self.selector.addWidget(self.target_file_path_label)
        self.selector_widget.setLayout(self.selector)

        self.layout.addWidget(self.selector_widget)

        self.setLayout(self.layout)

    def InfoSelector(self):
        '''
        A grid layout that contains 3 dropdowns
        '''
        layout = QGridLayout()
        layout.addWidget(QLabel("Select Folder"), 0, 0)
        layout.addWidget(QLabel("Select Section"), 0, 1)
        folder_options = QComboBox()
        folder_list = self.GetSub("ResumeGenerator/Informations")
        self.target_folder_list = folder_list
        folder_options.addItem("SELECT A FOLDER:")
        folder_options.addItems(folder_list)
        folder_options.setCurrentIndex(0)
        folder_options.currentIndexChanged.connect(self.folder_selected)
        layout.addWidget(folder_options, 1, 0)
        # self.folder_options = QComboBox()
        # self.folder_options.addItems(self.folder_list)
        # self.folder_options.currentIndexChanged.connect(self.folder_selected)
        # self.folder_options.setCurrentIndex(0)
        return layout

    def File_Sel(self) -> QComboBox:
        file_options = QComboBox()
        file_options.addItem("SELECT A FILE:")
        file_options.setCurrentIndex(0)
        file_options.addItems(self.target_file_list)
        file_options.currentIndexChanged.connect(self.FileSelected)
        old_item = self.info_selector.itemAtPosition(1, 1)
        if old_item:
            widget = old_item.widget()  # Retrieve the widget at the position
            if widget:
                widget.deleteLater()
        self.info_selector.addWidget(file_options, 1, 1)

    def folder_selected(self, index) -> None:
        if(index != 0):

            selected_item = self.target_folder_list[index-1]
            self.target_folder = selected_item
            folder_path = "ResumeGenerator/Informations/" + selected_item
            self.target_file_list = self.GetFileList(folder_path)
            self.File_Sel()
        else:
            old_item = self.info_selector.itemAtPosition(1, 1)
            if old_item:
                widget = old_item.widget()  # Retrieve the widget at the position
                if widget:
                    widget.deleteLater()

    def GetSub(self, rel_path:str) -> list:
        '''
        To use this, path starts from ResumeGenerator/...
        '''
        abs_file_path = os.path.abspath(rel_path)
        folder_names = [
            name
            for name in os.listdir(abs_file_path)
            if os.path.isdir(os.path.join(abs_file_path, name))
        ]
        return folder_names

    def GetFileList(self, rel_path):
        folder_path = os.path.abspath(rel_path)
        if not os.path.isabs(folder_path):
            raise ValueError("The provided path must be an absolute path.")
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"The path '{folder_path}' is not a valid directory.")

        # List comprehension to filter out directories
        return [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]

    def ModFile(self):
        '''
        Modify file structure, implement in stage 3
        '''

    def FileSelected(self, index):
        '''
        not yet implemented
        '''
        if index != 0:
            self.target_file = self.target_file_list[index-1]
            self.target_file_path = "ResumeGenerator/Informations/" + self.target_folder + "/" +  self.target_file
            self.target_file_path_label.setText(self.target_file_path)
