from PyQt6 import QtWidgets

from model.Cargo import Cargo
from services.CargoServicioImpl import crearCargo, actualizarCargo, obtenerCargo, eliminarCargo
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_cargo import Ui_Frame


class CargoController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnCrearCargo.clicked.connect(self.crear_cargo)
        self.btnBuscarCargo.clicked.connect(self.buscar_cargo)
        self.btnEditarCargo.clicked.connect(self.aditar_cargo)
        self.btnEliminarCargo.clicked.connect(self.eliminar_cargo)

    def crear_cargo(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        salario = self.tfSalario.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if salario == '':
            mensaje_error("El campo salario es requerido")
            return

        try:
            crearCargo(codigo, nombre, salario)
            mensaje_informacion("Cargo creado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_cargo(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        try:
            cargo = obtenerCargo(codigo)
            self.llenar_campos(cargo)
            mensaje_informacion("Cargo encontrado exitosamente")
        except Exception as e:
            mensaje_error(str(e))

    def aditar_cargo(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        salario = self.tfSalario.text().strip()

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if salario == '':
            mensaje_error("El campo salario es requerido")
            return

        try:
            actualizarCargo(codigo, nombre, salario)
            mensaje_informacion("Cargo actualizado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_cargo(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        try:
            eliminarCargo(codigo)
            mensaje_informacion("Cargo eliminado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def llenar_campos(self, cargo):
        self.tfCodigo.setText(cargo.codigoCargo)
        self.tfNombre.setText(cargo.nombreCargo)
        self.tfSalario.setText(str(cargo.salarioCargo))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")
        self.tfSalario.setText("")