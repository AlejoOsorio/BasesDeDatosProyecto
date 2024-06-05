from PyQt6 import QtWidgets

from services.DepartamentoServicioImpl import obtenerListaDepartamentos
from services.MunicipioServicioImpl import crearMunicipio, actualizarMunicipio, obtenerMunicipio, eliminarMunicipio
from services.PrioridadServicioImpl import obtenerListaPrioridades
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_municipio import Ui_Frame


class MunicipioController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_combobox()
        self.btnCrearMunicipio.clicked.connect(self.crear_municipio)
        self.btnBuscarMunicipio.clicked.connect(self.buscar_municipio)
        self.btnActualizarMunicipio.clicked.connect(self.actualizar_municipio)
        self.btnEliminarMunicipio.clicked.connect(self.eliminar_municipio)

    def showEvent(self, event):
        super().showEvent(event)
        self.llenar_combobox()

    def crear_municipio(self):
        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        poblacion = self.tfPoblacion.text().strip()
        tipo_municipio = self.cbTipoMunicipio.itemData(self.cbTipoMunicipio.currentIndex())
        departamento = self.cbDepartamento.itemData(self.cbDepartamento.currentIndex())

        if codigo == '':
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
            crearMunicipio(codigo, nombre, tipo_municipio, departamento, poblacion)
            mensaje_informacion("Municipio creado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_municipio(self):
        codiogo = self.tfCodigo.text().strip()

        if codiogo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            municipio = obtenerMunicipio(codiogo)
            self.llenar_campos(municipio)
            mensaje_informacion("Municipio encontrado correctamente")
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_municipio(self):
        codiogo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        poblacion = self.tfPoblacion.text().strip()
        tipo_municipio = self.cbTipoMunicipio.itemData(self.cbTipoMunicipio.currentIndex())
        departamento = self.cbDepartamento.itemData(self.cbDepartamento.currentIndex())

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
            actualizarMunicipio(codiogo, nombre, tipo_municipio, departamento, poblacion)
            mensaje_informacion("Municipio actualizado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_municipio(self):
        codiogo = self.tfCodigo.text().strip()

        if codiogo == '':
            mensaje_error("El campo codigo es requerido")
            return

        try:
            eliminarMunicipio(codiogo)
            mensaje_informacion("Municipio encontrado correctamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfNombre.setText("")
        self.tfPoblacion.setText("")

    def llenar_campos(self, municipio):
        self.tfCodigo.setText(municipio.codigoMunicipio)
        self.tfNombre.setText(municipio.nombreMunicipio)
        self.tfPoblacion.setText(str(municipio.poblacionMunicipio))
        index_tipo_municipio = self.cbTipoMunicipio.findData(municipio.prioridad)
        index_departamento = self.cbDepartamento.findData(municipio.departamento)

        if index_tipo_municipio != -1:
            self.cbTipoMunicipio.setCurrentIndex(index_tipo_municipio)
        if index_departamento != -1:
            self.cbDepartamento.setCurrentIndex(index_departamento)

    def llenar_combobox(self):
        try:
            self.cbTipoMunicipio.clear()
            self.cbDepartamento.clear()
            tipo_municipios = obtenerListaPrioridades()
            departamentos = obtenerListaDepartamentos()

            for tipo_municipio in tipo_municipios:
                self.cbTipoMunicipio.addItem(tipo_municipio.nombrePrioridad, tipo_municipio.codigoPrioridad)

            for departamento in departamentos:
                self.cbDepartamento.addItem(departamento.nombreDepartamento, departamento.codigoDepartamento)
        except Exception as e:
            print(e)
