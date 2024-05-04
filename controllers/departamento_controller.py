from PyQt6 import QtWidgets

from views.python_files.frame_departamento import Ui_Frame


class DepartamentoController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
