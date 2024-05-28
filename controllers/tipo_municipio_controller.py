from PyQt6 import QtWidgets

from services.PrioridadServicioImpl import crearPrioridad, obtenerPrioridad, actualizarPrioridad, eliminarPrioridad
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_tipo_municipio import Ui_Frame


class TipoMunicipioController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnCrearTipoMunicipio.clicked.connect(self.crear_tipo_municipio)
        self.btnBuscarTipoMunicipio.clicked.connect(self.buscar_tipo_municipio)
        self.btnActualizarTipoMunicipio.clicked.connect(self.actualizar_tipo_municipio)
        self.btnEliminarTipoMunicipio.clicked.connect(self.eliminar_tipo_municipio)

    def crear_tipo_municipio(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == "":
            mensaje_error("El campo nombre es requerido")
            return

        try:
            crearPrioridad(codigo, nombre)
            mensaje_informacion("EL tipo municipio se ha creado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_tipo_municipio(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return

        try:
            tipo_municipio = obtenerPrioridad(codigo)
            mensaje_informacion("EL tipo municipio se ha encontrado correctamente")
            self.llenar_campos(tipo_municipio)
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_tipo_municipio(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return
        if nombre == "":
            mensaje_error("El campo nombre es requerido")
            return

        try:
            actualizarPrioridad(codigo, nombre)
            mensaje_informacion("EL tipo municipio se ha actualizado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_tipo_municipio(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == "":
            mensaje_error("El campo codigo es requerido")
            return

        try:
            eliminarPrioridad(codigo)
            mensaje_informacion("EL tipo municipio se ha eliminado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")

    def llenar_campos(self, tipo_municipio):
        self.tfCodigo.setText(tipo_municipio.codigoPrioridad)
        self.tfNombre.setText(tipo_municipio.nombrePrioridad)
