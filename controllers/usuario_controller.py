from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate

from views.python_files.frame_usuario import Ui_Frame


class UsuarioController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dpFechaCreacion.setDate(QDate.currentDate())
