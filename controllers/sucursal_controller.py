from PyQt6 import QtWidgets

from services.MunicipioServicioImpl import obtenerListaMunicipios
from services.SucursalServicioImpl import crearSucursal, actualizarSucursal, obtenerSucursal, eliminarSucursal
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_sucursal import Ui_Frame


class SucursalController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_combobox()
        self.btnCrearSucursal.clicked.connect(self.crear_sucursal)
        self.btnBuscarSucursal.clicked.connect(self.buscar_sucursal)
        self.btnActualizarSucursal.clicked.connect(self.actualizar_sucursal)
        self.btnEliminarSucursal.clicked.connect(self.eliminar_sucursal)

    def showEvent(self, event):
        super().showEvent(event)
        self.llenar_combobox()

    def crear_sucursal(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        presupuesto = self.tfPresupuestoAnual.text().strip()
        direccion = self.tfDireccion.text().strip()
        telefono = self.tfTelefono.text().strip()
        municipio = self.cbMunicipio.itemData(self.cbMunicipio.currentIndex())

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if presupuesto == '':
            mensaje_error("El campo presupuesto es requerido")
            return
        if direccion == '':
            mensaje_error("El campo direccion es requerido")
            return
        if telefono == '':
            mensaje_error("El campo telefono es requerido")
            return

        try:
            crearSucursal(codigo, nombre, presupuesto, direccion, telefono, municipio)
            mensaje_informacion("Sucursal creada correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_sucursal(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            sucursal = obtenerSucursal(codigo)
            mensaje_informacion("Sucursal obtenida correctamente")
            self.llenar_campos(sucursal)
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_sucursal(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        presupuesto = self.tfPresupuestoAnual.text().strip()
        direccion = self.tfDireccion.text().strip()
        telefono = self.tfTelefono.text().strip()
        municipio = self.cbMunicipio.itemData(self.cbMunicipio.currentIndex())

        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if presupuesto == '':
            mensaje_error("El campo presupuesto es requerido")
            return
        if direccion == '':
            mensaje_error("El campo direccion es requerido")
            return
        if telefono == '':
            mensaje_error("El campo telefono es requerido")
            return

        try:
            actualizarSucursal(codigo, nombre, presupuesto, direccion, telefono, municipio)
            mensaje_informacion("Sucursal actualizada correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_sucursal(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            eliminarSucursal(codigo)
            mensaje_informacion("Sucursal eliminada correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")
        self.tfPresupuestoAnual.setText("")
        self.tfDireccion.setText("")
        self.tfTelefono.setText("")

    def llenar_campos(self, sucursal):
        self.tfCodigo.setText(sucursal.codigoSucursal)
        self.tfNombre.setText(sucursal.nombreSucursal)
        self.tfPresupuestoAnual.setText(str(sucursal.presupuestoAnual))
        self.tfDireccion.setText(sucursal.direccionSucursal)
        self.tfTelefono.setText(sucursal.telefono)
        index_municipio = self.cbMunicipio.findData(sucursal.municipio)
        if index_municipio != -1:
            self.cbMunicipio.setCurrentIndex(index_municipio)

    def llenar_combobox(self):
        try:
            self.cbMunicipio.clear()
            municipios = obtenerListaMunicipios()

            for municipio in municipios:
                self.cbMunicipio.addItem(municipio.nombreMunicipio, municipio.codigoMunicipio)
        except Exception as e:
            print(e)
