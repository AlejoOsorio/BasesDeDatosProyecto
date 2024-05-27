from PyQt6 import QtWidgets

from controllers.main_window_controller import MainWindowController
from model.NivelUsuario import NivelUsuario
from model.Usuairo import Usuario
from utils.utils_qt import mensaje_error
from views.python_files.frame_login_usuario import Ui_Frame


class LogInController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.usuarios = [
            Usuario("ramon", "123", NivelUsuario.ESPORADICO),
            Usuario("pedro", "123", NivelUsuario.PARAMETRICO),
            Usuario("manuel", "123", NivelUsuario.PARAMETRICO),
            Usuario("pablo", "123", NivelUsuario.PRINCIPAL)
        ]

        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        usuario = self.tfEmail.text()
        password = self.tfPassword.text()

        for us in self.usuarios:
            if us.login == usuario:
                if us.password == password:
                    MainWindowController(us).show()
                    self.close()
                    return
                else:
                    mensaje_error("Contraseña incorrecta")
                    return

        mensaje_error("Usuario no encontrado")
