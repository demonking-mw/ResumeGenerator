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

from . import view_info
from . import mod_info


class ViewMod(QWidget):
    def __init__(self):

        super().__init__()
        self.layout = QVBoxLayout()
        self.stack = QStackedWidget()

        self.mod_info = mod_info.ModInfo(self.switch_page)
        self.view_info = view_info.ViewInfo(self.switch_page, self.mod_info.communicate)
        
        self.stack.addWidget(self.view_info)
        self.stack.addWidget(self.mod_info)
        self.stack.setCurrentIndex(0)

        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
