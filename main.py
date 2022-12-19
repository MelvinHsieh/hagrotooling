import sys

from PyQt5.QtWidgets import QApplication

# Run the main loop
from scripts.pdfimportwindow import PdfImportWindow
from scripts.configurationcreatorwindow import ConfigurationCreatorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    configuration_creator_window = ConfigurationCreatorWindow()

    # Todo: This window, or at least the tabula load pdf function, should be ran on a different thread to not-freeze
    #  the app.
    pdf_import_window = PdfImportWindow()

    sys.exit(app.exec_())
