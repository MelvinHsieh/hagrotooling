import sys
import tabula

from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QProgressBar

# Create the main window

app = QApplication(sys.argv)
window = QWidget()
window.setMinimumSize(300, 200)
window.setWindowTitle("Hagrotooling")
window.setStyleSheet("QWidget {background-color: #2b2b2b; color: white;} QPushButton {background-color: #3592c4;}")

# Create layout
layout = QVBoxLayout()

# Create a label and set its text
label = QLabel("U heeft nog geen PDF bedstanden geselecteerd.")
layout.addWidget(label)

# Create a button to open the file selection dialog
button = QPushButton("Selecteer PDF bestanden")
layout.addWidget(button)


# Create a function to handle the button click event
def on_button_clicked():
    # Open the file selection dialog
    file_names, _ = QFileDialog.getOpenFileNames(window, "Selecteer PDF bestanden met materiaaltabellen", "",
                                                 "PDF Files (*.pdf)")

    # Update the label text
    label.setText("Geselecteerde PDF bestanden:\n" + "\n".join(file_names))
    load_pdf(file_names)


def load_pdf(file_names):
    # read the PDF file using tabula
    tables = tabula.read_pdf(file_names[0], stream=True, pages="all", multiple_tables=True)

    for table in tables:
        print(table)


# Connect the button click event to the function
button.clicked.connect(on_button_clicked)

# Show the main window
window.setLayout(layout)
window.show()

# Run the main loop
sys.exit(app.exec_())
