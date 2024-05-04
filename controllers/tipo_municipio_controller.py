from PyQt6 import QtWidgets
from views.python_files.frame_tipo_municipio import Ui_Frame


class TipoMunicipioController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
