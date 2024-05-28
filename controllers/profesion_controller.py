from PyQt6 import QtWidgets

from services.ProfesionServicioImpl import crearProfesion, actualizarProfesion, obtenerProfesion, eliminarProfesion
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_profesion import Ui_Frame


class ProfesionController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnCrearProfesion.clicked.connect(self.crear_profesion)
        self.btnBuscarProfesion.clicked.connect(self.buscar_profesion)
        self.btnActualizarProfesion.clicked.connect(self.actualizar_profesion)
        self.btnEliminarProfesion.clicked.connect(self.eliminar_profesion)

    def crear_profesion(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return

        try:
            crearProfesion(codigo, nombre)
            mensaje_informacion("profesión creada exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_profesion(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            profesion = obtenerProfesion(codigo)
            self.llenar_campos(profesion)
            mensaje_informacion("profesión obtenida exitosamente")
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_profesion(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return

        try:
            actualizarProfesion(codigo, nombre)
            mensaje_informacion("profesión actualizada exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_profesion(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            eliminarProfesion(codigo)
            mensaje_informacion("profesión eliminada exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")

    def llenar_campos(self, profesion):
        self.tfCodigo.setText(profesion.codigoProfesion)
        self.tfNombre.setText(profesion.nombreProfesion)
