from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class ConfigurationCreatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        info_label = QLabel("Hier kan u nieuwe configuraties toepassen voor pdfs per fabrikant of gereedschap.")

        # Create a vertical layout to hold the buttons
        vbox = QVBoxLayout()
        vbox.addWidget(info_label)

        # Set the layout of the main window
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(300, 300, 300, 150)
        self.setMinimumSize(500, 200)
        self.setWindowTitle("Hagro Material Master")
        self.setStyleSheet("QWidget {background-color: #2b2b2b; color: white;} QPushButton {background-color: #3592c4;}")
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)

        self.show()