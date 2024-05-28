import datetime

from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QTableView

from services.CargoServicioImpl import obtenerListaCargos
from services.ContratoServicioImpl import crearContrato, actualizarContrato, obtenerContrato, eliminarContrato
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
        self.btnActualizarContrato.clicked.connect(self.actualizar_contrato)
        self.btnBuscarContrato.clicked.connect(self.buscar_contrato)
        self.btnEliminarContrato.clicked.connect(self.eliminar_contrato)
        self.dpFechaContrato.setDate(QDate.currentDate())
        self.dpFechaInicioContrato.setDate(QDate.currentDate())
        self.dpFechaTerminacionContrato.setDate(QDate.currentDate())

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
        formato = "%d/%m/%Y"

        codigo = self.tfCodigo.text().strip()
        fechaContrato = datetime.datetime.strptime(self.dpFechaContrato.text(), formato)
        fechaInicioContrato = datetime.datetime.strptime(self.dpFechaInicioContrato.text(), formato)
        fechaTerminacionContrato = datetime.datetime.strptime(self.dpFechaTerminacionContrato.text(), formato)
        sucursal = self.sucursal_codigos[self.cbSucursales.currentText()]
        cargo = self.cargos_codigos[self.cbCargos.currentText()]
        empleado = self.tvEmpleados.selectionModel()

        if empleado.hasSelection():
            indexes = empleado.selectedIndexes()
            codigoEmpleado = self.model.itemFromIndex(indexes[0]).text()
        else:
            mensaje_error("Es necesario que seleccione un Empleado")
            return
        if codigo == "":
            mensaje_error("Es necesario que digite el código")
            return

        try:
            crearContrato(codigo, fechaContrato, fechaInicioContrato, fechaTerminacionContrato, codigoEmpleado,
                          sucursal, cargo)
        except Exception as e:
            mensaje_error(e)

    def actualizar_contrato(self):
        formato = "%d/%m/%Y"

        codigo = self.tfCodigo.text().strip()
        fechaContrato = datetime.datetime.strptime(self.dpFechaContrato.text(), formato)
        fechaInicioContrato = datetime.datetime.strptime(self.dpFechaInicioContrato.text(), formato)
        fechaTerminacionContrato = datetime.datetime.strptime(self.dpFechaTerminacionContrato.text(), formato)
        sucursal = self.sucursal_codigos[self.cbSucursales.currentText()]
        cargo = self.cargos_codigos[self.cbCargos.currentText()]
        empleado = self.tvEmpleados.selectionModel()

        if empleado.hasSelection():
            indexes = empleado.selectedIndexes()
            codigoEmpleado = self.model.itemFromIndex(indexes[0]).text()
        else:
            mensaje_error("Es necesario que seleccione un Empleado")
            return
        if codigo == "":
            mensaje_error("Es necesario que digite el código")
            return

        try:
            actualizarContrato(codigo, fechaContrato, fechaInicioContrato, fechaTerminacionContrato, codigoEmpleado,
                               sucursal, cargo)
        except Exception as e:
            mensaje_error(e)

    def buscar_contrato(self):
        codigo = self.tfCodigo.text().strip()

        if codigo == "":
            mensaje_error("Es necesario que digite el código")
            return

        try:
            contrato = obtenerContrato(codigo)
            self.setear_datos(contrato)
        except Exception as e:
            print(e)
            mensaje_error(str(e))

    def eliminar_contrato(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == "":
            mensaje_error("Es necesario que digite el código")
            return
        try:
            eliminarContrato(codigo)
        except Exception as e:
            mensaje_error(str(e))

    def setear_datos(self, contrato):
        self.dpFechaContrato.setDate(QDate.fromString(str(contrato.fechaContrato), "yyyy-MM-dd"))
        self.dpFechaInicioContrato.setDate(QDate.fromString(str(contrato.fechaInicioContrato), "yyyy-MM-dd"))
        self.dpFechaTerminacionContrato.setDate(QDate.fromString(str(contrato.fechaTerminacionContrato), "yyyy-MM-dd"))
        index_sucursal = self.cbSucursales.findText(self.obtener_llave_por_valor(self.sucursal_codigos, contrato.sucursal))
        index_cargo = self.cbCargos.findText(self.obtener_llave_por_valor(self.cargos_codigos, contrato.cargo))
        if index_sucursal != -1:
            self.cbSucursales.setCurrentIndex(index_sucursal)
        if index_cargo != -1:
            self.cbCargos.setCurrentIndex(index_cargo)

        valor_buscado = contrato.empleado
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 0)  # Obtener el índice de la columna uno
            if self.model.data(index, Qt.ItemDataRole.DisplayRole) == valor_buscado:
                self.tvEmpleados.selectRow(row)
                break

    def obtener_llave_por_valor(self, diccionario, valor):
        for key, val in diccionario.items():
            if val == valor:
                return key
        return None