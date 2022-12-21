import json

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                             QPushButton, QWidget, QFileDialog)


class ConfigurationCreatorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(400)
        self.setWindowTitle("Hagro Pdf Configuration Creator")
        self.setStyleSheet("QWidget {background-color: #2b2b2b; color: white;} QPushButton {background-color: #3592c4;}")
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)

        # Create a label and text field for the file name
        name_label = QLabel("Configuratiebestandsnaam:")
        self.name_field = QLineEdit()

        # Create a button to add more text fields
        add_button = QPushButton("Voeg kolom toe")
        add_button.clicked.connect(self.add_text_field)

        # Create a button to save the data to a JSON file
        save_button = QPushButton("Opslaan")
        save_button.clicked.connect(self.save_data)

        # Create a button for loading the data
        load_button = QPushButton("Inladen")
        load_button.clicked.connect(self.load_data)

        # Create a layout to hold the widgets
        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_field, 0, 1)
        layout.addWidget(add_button, 1, 0)
        layout.addWidget(save_button, 1, 1)
        layout.addWidget(load_button)
        self.setLayout(layout)

        # Create a list to hold the text fields
        self.text_fields = []

        self.show()

    def add_text_field(self):
        # Create a new text field and add it to the layout
        text_field = QLineEdit()
        layout = self.layout()
        num_rows = layout.rowCount()
        layout.addWidget(text_field, num_rows, 0, 1, 2)

        # Add the text field to the list
        self.text_fields.append(text_field)

    def save_data(self):
        # Get the name from the name field
        name = self.name_field.text()

        # Create a dictionary to hold the data
        data = {}

        # Add the text fields to the dictionary
        for i, text_field in enumerate(self.text_fields):
            data[f'column_{i}'] = text_field.text()

        # Convert the dictionary to JSON
        json_data = json.dumps(data)

        # Save the JSON data to a file
        file_name = f"{name}.json"
        with open("configurations/" + file_name, "w") as f:
            f.write(json_data)

    def load_data(self):
        # Use a file dialog to allow the user to select a JSON file to load
        file_name, _ = QFileDialog.getOpenFileName(self, "Open JSON file", "", "JSON files (*.json)")

        # If a file was selected, load the data from the file
        if file_name:
            with open(file_name, "r") as f:
                data = json.load(f)

            # Set the name field to the name of the file (without the ".json" extension)
            self.name_field.setText(file_name.split('/')[-1][:-5])

            # Clear the current text fields
            for text_field in self.text_fields:
                text_field.deleteLater()
            self.text_fields = []

            print(data)
            # Add new text fields with the data from the file
            for key, value in data.items():
                text_field = QLineEdit()
                text_field.setText(value)
                layout = self.layout()
                num_rows = layout.rowCount()
                layout.addWidget(text_field, num_rows, 0, 1, 2)

                # Add the text field to the list
                self.text_fields.append(text_field)
