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


from . import main_page


class MainWindow(QMainWindow):
    # python -m ResumeGenerator.UI.app.application
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grass Allergy Relief")
        self.setGeometry(100, 50, 500, 550)

        # Create the central widget
        self.central_widget = main_page.MainPage()
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
