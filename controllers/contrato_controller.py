from PyQt6 import QtWidgets
from views.python_files.frame_contrato import Ui_Frame


class ContratoController(QtWidgets.QWidget, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
