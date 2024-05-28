from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate

from model.NivelUsuario import NivelUsuario
from services.UsuarioServicioImpl import crearUsuario, actualizarUsuario, obtenerUsuario, eliminarUsuario
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_usuario import Ui_Frame


class UsuarioController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_combobox()
        self.dpFechaCreacion.setDate(QDate.currentDate())
        self.btnCrearUsuario.clicked.connect(self.crear_usuario)
        self.btnBuscarUsuario.clicked.connect(self.buscar_usuario)
        self.btnActualizarUsuario.clicked.connect(self.actualizar_usuario)
        self.btnEliminarUsuairo.clicked.connect(self.eliminar_usuario)

    def crear_usuario(self):
        codigo = self.tfCodigo.text().strip()
        user = self.tfUser.text().strip()
        password = self.tfPassword.text().strip()
        nivelUsuario = self.cbNivelUsuario.currentText()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if user == '':
            mensaje_error("El campo user es requerido")
            return
        if password == '':
            mensaje_error("El campo password es requerido")
            return

        try:
            crearUsuario(codigo, user, password, nivelUsuario)
            mensaje_informacion("Usuario creado correctamente")
            self.limpiar_campos()
        except Exception as e:
            print(e)
            mensaje_error(str(e))

    def buscar_usuario(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        try:
            usuario = obtenerUsuario(codigo)
            self.llenar_campos(usuario)
            mensaje_informacion("Usuario encontrado correctamente")
        except Exception as e:
            print(e)
            mensaje_error(str(e))

    def actualizar_usuario(self):
        codigo = self.tfCodigo.text().strip()
        user = self.tfUser.text().strip()
        password = self.tfPassword.text().strip()
        nivelUsuario = self.cbNivelUsuario.currentText()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if user == '':
            mensaje_error("El campo user es requerido")
            return
        if password == '':
            mensaje_error("El campo password es requerido")
            return

        try:
            actualizarUsuario(codigo, user, password, nivelUsuario)
            mensaje_informacion("Usuario actualizado correctamente")
            self.limpiar_campos()
        except Exception as e:
            print(e)
            mensaje_error(str(e))

    def eliminar_usuario(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        try:
            eliminarUsuario(codigo)
            mensaje_informacion("Usuario eliminado correctamente")
            self.limpiar_campos()
        except Exception as e:
            print(e)
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfUser.setText("")
        self.tfPassword.setText("")

    def llenar_campos(self, usuario):
        self.tfCodigo.setText(usuario.codigoUsuario)
        self.tfUser.setText(usuario.nombreUsuario)
        self.tfPassword.setText(usuario.claveUsuario)
        index_nivel = self.cbNivelUsuario.findText(usuario.nivelUsuario)
        if index_nivel != -1:
            self.cbNivelUsuario.setCurrentIndex(index_nivel)

    def llenar_combobox(self):
        try:
            nivelesUsuario = [nivel.value for nivel in NivelUsuario]

            for nivel in nivelesUsuario:
                self.cbNivelUsuario.addItem(nivel)
        except Exception as e:
            print(e)
