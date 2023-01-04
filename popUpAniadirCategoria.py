import sys

from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog
from PyQt5 import QtWidgets, uic
from PyQt5.uic.properties import QtCore


from ventanaAniadirCategoria_ui import Ui_Dialog


class nuevaCategoria(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


        self.ui.aniadirCategoria_btnAniadir.clicked.connect(self.aniadirNuevaCategoria)



    def aniadirNuevaCategoria(self):
        nombreNuevaCategoria = self.ui.aniadirCategoria_nombreCategoria.text()
        print(nombreNuevaCategoria)

