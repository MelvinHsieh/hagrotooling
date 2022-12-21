import tabula

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget


# Create the main window
class PdfImportWindow(QWidget):
    def __init__(self):
        self.file_names = None
        self.window = QWidget()
        self.info_label = QLabel("Hier kan u pdf's selecteren en daarbij tabellen inlezen.")
        self.label = QLabel("U heeft nog geen PDF bedstanden geselecteerd.")
        super().__init__()
        self.initUI()

    def initUI(self):
        self.window.setMinimumSize(300, 200)
        self.window.setWindowTitle("Hagro Pdf Importer")
        self.window.setStyleSheet("QWidget {background-color: #2b2b2b; color: white;} QPushButton {background-color: #3592c4;}")
        icon = QIcon("icon.png")
        self.window.setWindowIcon(icon)

        # Create layout
        layout = QVBoxLayout()

        # Create a label and set its text
        layout.addWidget(self.info_label)
        layout.addWidget(self.label)

        # Create a button to open the file selection dialog
        button = QPushButton("Selecteer PDF bestanden")
        layout.addWidget(button)

        # Connect the button click event to the function
        button.clicked.connect(self.on_button_clicked)

        # Show the main window
        self.window.setLayout(layout)
        self.window.show()

    # Create a function to handle the button click event
    def on_button_clicked(self):
        # Open the file selection dialog
        self.file_names, _ = QFileDialog.getOpenFileNames(self.window, "Selecteer PDF bestanden met materiaaltabellen", "",
                                                     "PDF Files (*.pdf)")

        # Update the label text
        self.label.setText("Geselecteerde PDF bestanden:\n" + "\n".join(self.file_names))
        self.load_pdf()

    def load_pdf(self):
        # read the PDF file using tabula
        tables = tabula.read_pdf(self.file_names[0], stream=True, pages="all", multiple_tables=True, guess=True)

        # TODO: Some tables have the second row as their "column" header.
        # TODO: For example, see testdata "fraeskatalog....pdf", page 338.

        # TODO: The identifying column name is on the second row, it's called W-Nr. Mat.-No.

        # To write to "csv" instead, replace the filename .json to csv, and the output format from json to csv.
        for i, table in enumerate(tables):
            file_name = f'table_{i}.json'
            # Write the table to the file
            tabula.convert_into(self.file_names[0], file_name, output_format="json", pages=i + 1)
            print(f'Successfully wrote table {i} to {file_name}')
