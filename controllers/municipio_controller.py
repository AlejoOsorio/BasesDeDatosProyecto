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

    def crear_municipio(self):

        codigo = self.tfCodigo.text().strip()
        nombre = self.tfNombre.text().strip()
        poblacion = self.tfPoblacion.text().strip()
        tipoMunicipio = self.tipoMunicipiosCodigos[self.cbTipoMunicipio.currentText()]
        departamento = self.departamentoCodigos[self.cbDepartamento.currentText()]

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
            crearMunicipio(codigo, nombre, tipoMunicipio, departamento, poblacion)
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
        tipoMunicipio = self.tipoMunicipiosCodigos[self.cbTipoMunicipio.currentText()]
        departamento = self.departamentoCodigos[self.cbDepartamento.currentText()]

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
            actualizarMunicipio(codiogo, nombre, tipoMunicipio, departamento, poblacion)
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
        index_tipo_municipio = self.cbTipoMunicipio.findText(
            self.obtener_llave_por_valor(self.tipoMunicipiosCodigos, municipio.prioridad))
        index_departamento = self.cbDepartamento.findText(self.obtener_llave_por_valor(self.departamentoCodigos, municipio.departamento))
        if index_tipo_municipio != -1:
            self.cbTipoMunicipio.setCurrentIndex(index_departamento)
        if index_departamento != -1:
            self.cbDepartamento.setCurrentIndex(index_departamento)

    def llenar_combobox(self):
        try:
            tipoMunicipios = obtenerListaPrioridades()
            departamentos = obtenerListaDepartamentos()
            self.tipoMunicipiosCodigos = {}
            self.departamentoCodigos = {}

            for tipoMunicipio in tipoMunicipios:
                self.tipoMunicipiosCodigos[tipoMunicipio.nombrePrioridad] = tipoMunicipio.codigoPrioridad
            for departamento in departamentos:
                self.departamentoCodigos[departamento.nombreDepartamento] = departamento.codigoDepartamento

            for key_tipo_municipio in self.tipoMunicipiosCodigos.keys():
                self.cbTipoMunicipio.addItem(key_tipo_municipio)

            for key_departamento in self.departamentoCodigos.keys():
                self.cbDepartamento.addItem(key_departamento)
        except Exception as e:
            print(e)

    def obtener_llave_por_valor(self, diccionario, valor):
        for key, val in diccionario.items():
            if val == valor:
                return key
        return None
