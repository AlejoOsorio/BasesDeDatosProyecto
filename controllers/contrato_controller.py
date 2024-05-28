import datetime

from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QTableView

from services.CargoServicioImpl import obtenerListaCargos
from services.ContratoServicioImpl import crearContrato
from services.EmpleadoServicioImpl import obtenerListaEmpleados
from services.SucursalServicioImpl import obtenerListaSucursal
from utils.utils_qt import mensaje_error
from views.python_files.frame_contrato import Ui_Frame


class ContratoController(QtWidgets.QWidget, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_tabla()
        self.llenar_combobox()
        self.btnCrearContrato.clicked.connect(self.crear_contrato)

    def llenar_tabla(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Código', 'Nombre'])
        empleados = obtenerListaEmpleados()

        data = []
        for empleado in empleados:
            data.append([empleado.codigoEmpleado, empleado.nombreEmpleado])

        for row in data:
            items = [QStandardItem(field) for field in row]
            for item in items:
                item.setEditable(False)
            self.model.appendRow(items)

        self.tvEmpleados.setModel(self.model)

        header = self.tvEmpleados.horizontalHeader()
        header.setStretchLastSection(True)

        self.btnCrearContrato.clicked.connect(self.capturar_dato_tabla)

        self.tvEmpleados.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

    def capturar_dato_tabla(self):
        selection_model = self.tvEmpleados.selectionModel()

        if selection_model.hasSelection():
            indexes = selection_model.selectedIndexes()
            item = self.model.itemFromIndex(indexes[0])

    def llenar_combobox(self):
        try:
            sucursales = obtenerListaSucursal()
            cargos = obtenerListaCargos()
            self.cargos_codigos = {}
            self.sucursal_codigos = {}

            for cargo in cargos:
                self.cargos_codigos[cargo.nombreCargo] = cargo.codigoCargo

            for sucursal in sucursales:
                self.sucursal_codigos[sucursal.nombreSucursal] = sucursal.codigoSucursal

            for key_sucursal in self.sucursal_codigos.keys():
                self.cbSucursales.addItem(key_sucursal)

            for key_cargo in self.cargos_codigos.keys():
                self.cbCargos.addItem(key_cargo)

        except Exception as e:
            print(e)

    def crear_contrato(self):
        codigo = self.tfCodigo.text()
        formato = "%d/%m/%Y"
        try:
            fechaContrato = datetime.datetime.strptime(self.dpFechaContrato.text(), formato)
            fechaInicioContrato = datetime.datetime.strptime(self.dpFechaInicioContrato.text(), formato)
            fechaTerminacionContrato = datetime.datetime.strptime(self.dpFechaTerminacionContrato.text(), formato)
        except Exception as e:
            print(e)
        sucursal = self.sucursal_codigos[self.cbSucursales.currentText()]
        cargo = self.cargos_codigos[self.cbCargos.currentText()]
        empleado = self.tvEmpleados.selectionModel()

        if empleado.hasSelection():
            indexes = empleado.selectedIndexes()
            item = self.model.itemFromIndex(indexes[0]).text()
        else:
            mensaje_error("Es necesario que seleccione un Empleado")
            return

        print(codigo)
        print(fechaContrato)
        print(fechaInicioContrato)
        print(fechaTerminacionContrato)
        print(sucursal)
        print(cargo)
        print(item)

        try:
            crearContrato(codigo, fechaContrato, fechaInicioContrato, fechaTerminacionContrato, item, sucursal, cargo)
        except Exception as e:
            print(e)
