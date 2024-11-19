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

from ...FileGenerator import resume_pdf_builder

from . import generate


class MainWindow(QMainWindow):
    # python -m ResumeGenerator.UI.app.application
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grass Allergy Relief")
        self.setGeometry(100, 100, 500, 500)

        # Create the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()

        # Set up a QStackedWidget to hold the pages
        self.stack = QStackedWidget()

        # Create pages
        self.page1 = self.create_page1()
        self.page2 = self.create_page2()

        # Add pages to the stack
        self.stack.addWidget(generate.Generate())
        self.stack.addWidget(self.page2)

        # Page selection button
        button_cont = QWidget(self)
        button_cont.setStyleSheet(
            """
            QWidget {
                border: 1px solid black; /* Border around the widget */
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

        self.central_widget.setLayout(main_layout)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)

    def create_page1(self):
        page = QWidget()
        layout = QVBoxLayout()

        label = QLabel("This is Page 1")
        button = QPushButton("Go to Page 2")
        button.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        layout.addWidget(label)
        layout.addWidget(button)
        page.setLayout(layout)
        return page

    def create_page2(self):
        page = QWidget()
        layout = QVBoxLayout()

        label = QLabel("This is Page 2")
        button = QPushButton("Go to Page 1")
        button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(label)
        layout.addWidget(button)
        page.setLayout(layout)
        return page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
