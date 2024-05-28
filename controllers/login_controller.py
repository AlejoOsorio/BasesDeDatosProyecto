from PyQt6 import QtWidgets

from controllers.main_window_controller import MainWindowController
from services.AuthServicioImpl import login
from utils.utils_qt import mensaje_error
from views.python_files.frame_login_usuario import Ui_Frame


class LogInController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        nickname = self.tfEmail.text()
        password = self.tfPassword.text()

        try:
            # usuario = login(nickname, password)
            usuario = login("admin", "admin123")
            MainWindowController(usuario).show()
            self.close()
        except Exception as e:
            print(e)
            mensaje_error(str(e))
