from PyQt6 import QtWidgets

from services.DepartamentoServicioImpl import crearDepartamento, actualizarDepartamento, obtenerDepartamento, \
    eliminarDepartamento
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_departamento import Ui_Frame


class DepartamentoController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnCrearDepartamento.clicked.connect(self.crear_departamento)
        self.btnActualizarDepartamento.clicked.connect(self.actualizar_departamento)
        self.btnBuscarDepartamento.clicked.connect(self.buscar_departamento)
        self.btnEliminarDepartamento.clicked.connect(self.eliminar_departamento)

    def crear_departamento(self):
        codiogo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        poblacion = self.tfPoblacion.text().strip()

        if codiogo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if poblacion == '':
            mensaje_error("El campo poblacion es requerido")
            return
        if not poblacion.isnumeric():
            mensaje_error("El campo poblacion debe de ser un numero valido")
            return

        try:
            crearDepartamento(codiogo, nombre, poblacion)
            mensaje_informacion("Departamento creado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_departamento(self):
        codiogo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        poblacion = self.tfPoblacion.text().strip()

        if codiogo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if poblacion == '':
            mensaje_error("El campo poblacion es requerido")
            return
        if not poblacion.isnumeric():
            mensaje_error("El campo poblacion debe de ser un numero valido")
            return

        try:
            actualizarDepartamento(codiogo, nombre, poblacion)
            mensaje_informacion("Departamento actualizado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_departamento(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return

        try:
            departamento = obtenerDepartamento(codigo)
            self.llenar_campos(departamento)
            mensaje_informacion("Departamento obtenido correctamente")
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_departamento(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return

        try:
            eliminarDepartamento(codigo)
            mensaje_informacion("Departamento eliminado correctamente")
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")
        self.tfPoblacion.setText("")

    def llenar_campos(self, departamento):
        self.tfCodigo.setText(departamento.codigoDepartamento)
        self.tfNombre.setText(departamento.nombreDepartamento)
        self.tfPoblacion.setText(str(departamento.poblacionDepartamento))
