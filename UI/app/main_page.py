from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QStackedWidget,
)
import sys


from . import generate
from . import view_info


class MainPage(QWidget):
    # python -m ResumeGenerator.UI.app.application
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Set up a QStackedWidget to hold the pages
        self.stack = QStackedWidget()

        # Add pages to the stack
        self.stack.addWidget(generate.Generate())
        self.stack.addWidget(view_info.ViewInfo())

        # Page selection button
        button_cont = QWidget(self)
        button_cont.setStyleSheet(
            """
            QWidget {
                border: 0px solid black; /* Border around the widget */
                background-color: darkgray; /* Background color */
                border-radius: 5px; /* Optional: rounded corners */
                padding: 15px; /* Padding inside the button */
            }
        """
        )
        button_layout = QHBoxLayout()
        buttons = [
            ("Generate Resume", 0),
            ("Modify Resume", 1),
        ]
        for label, index in buttons:
            button = QPushButton(label)
            button.setStyleSheet(
                """
            QPushButton {
                background-color: darkgray; /* Background color */
                border: 2px solid black; /* Border style */
                border-radius: 5px; /* Rounded corners */
                color: black; /* Text color */
                font-size: 12px; /* Font size */
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
            button.clicked.connect(lambda _, idx=index: self.switch_page(idx))
            button_layout.addWidget(button)
        button_cont.setLayout(button_layout)

        # Set up the main layout
        main_layout.addWidget(self.stack)
        main_layout.addWidget(button_cont)

        self.setLayout(main_layout)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
