from PyQt6 import QtWidgets

from controllers.main_window_controller import MainWindowController
from views.python_files.frame_login_usuario import Ui_Frame


class LogInController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dashboard = MainWindowController()
        self.buscar_3.clicked.connect(self.login)

    def login(self):
        self.dashboard.show()
        self.close()
