from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QTableView

from services.EmpleadoServicioImpl import crearEmpleado, actualizarEmpleado, obtenerEmpleado, eliminarEmpleado, \
    crearDetalleProfesion, eliminarProfesionesEmpleado
from services.ProfesionServicioImpl import obtenerListaProfesiones
from utils.utils_qt import mensaje_error, mensaje_informacion
from views.python_files.frame_empleado import Ui_Frame


class EmpleadoController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_tabla()
        self.btnCrearEmpleado.clicked.connect(self.crear_empleado)
        self.btnBuscarEmpleado.clicked.connect(self.buscar_empleado)
        self.btnActualizarEmpleado.clicked.connect(self.actualizar_empleado)
        self.btnEliminarEmpleado.clicked.connect(self.eliminar_empleado)

    def showEvent(self, event):
        super().showEvent(event)
        self.llenar_tabla()

    def crear_empleado(self):
        codigo = self.tfCodigo.text().strip()
        cedula = self.tfCedula.text().strip()
        nombre = self.tfNombre.text().strip()
        apellidos = self.tfApellidos.text().strip()
        email = self.tfEmail.text().strip()
        telefono = self.tfTelefono.text().strip()
        direccion = self.tfDireccion.text().strip()
        profesion = self.capturar_dato_tabla()

        if codigo == '':
            mensaje_error("El campo código es requerido")
            return
        if cedula == '':
            mensaje_error("El campo cédula es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if apellidos == '':
            mensaje_error("El campo apellidos es requerido")
            return
        if email == '':
            mensaje_error("El campo email es requerido")
            return
        if telefono == '':
            mensaje_error("El campo teléfono es requerido")
            return
        if direccion == '':
            mensaje_error("El campo dirección es requerido")
            return
        if profesion is None:
            mensaje_error("Seleccione una profesión")
            return

        try:
            crearEmpleado(codigo, cedula, nombre, apellidos, direccion, telefono, email)
            crearDetalleProfesion(codigo, profesion)
            mensaje_informacion("Empleado creado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def buscar_empleado(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo código es requerido")
            return
        try:
            empleado = obtenerEmpleado(codigo)
            self.llenar_campos(empleado)
            mensaje_informacion("Empleado encontrado exitosamente")
        except Exception as e:
            mensaje_error(str(e))

    def actualizar_empleado(self):
        codigo = self.tfCodigo.text().strip()
        cedula = self.tfCedula.text().strip()
        nombre = self.tfNombre.text().strip()
        apellidos = self.tfApellidos.text().strip()
        email = self.tfEmail.text().strip()
        telefono = self.tfTelefono.text().strip()
        direccion = self.tfDireccion.text().strip()
        profesion = self.capturar_dato_tabla()

        if codigo == '':
            mensaje_error("El campo código es requerido")
            return
        if cedula == '':
            mensaje_error("El campo cédula es requerido")
            return
        if nombre == '':
            mensaje_error("El campo nombre es requerido")
            return
        if apellidos == '':
            mensaje_error("El campo apellidos es requerido")
            return
        if email == '':
            mensaje_error("El campo email es requerido")
            return
        if telefono == '':
            mensaje_error("El campo teléfono es requerido")
            return
        if direccion == '':
            mensaje_error("El campo dirección es requerido")
            return
        if profesion is None:
            mensaje_error("Seleccione una profesión")

        try:
            actualizarEmpleado(codigo, cedula, nombre, apellidos, direccion, telefono, email)
            mensaje_informacion("Empleado actualizado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def eliminar_empleado(self):
        codigo = self.tfCodigo.text().strip()
        if codigo == '':
            mensaje_error("El campo código es requerido")
            return
        try:
            eliminarProfesionesEmpleado(codigo)
            eliminarEmpleado(codigo)
            mensaje_informacion("Empleado eliminado exitosamente")
            self.limpiar_campos()
        except Exception as e:
            mensaje_error(str(e))

    def limpiar_campos(self):
        self.tfCodigo.setText("")
        self.tfCedula.setText("")
        self.tfNombre.setText("")
        self.tfApellidos.setText("")
        self.tfEmail.setText("")
        self.tfTelefono.setText("")
        self.tfDireccion.setText("")
        self.tvProfesiones.selectionModel().clearSelection()

    def llenar_campos(self, empleado):
        self.tfCodigo.setText(empleado.codigoEmpleado)
        self.tfCedula.setText(empleado.cedulaEmpleado)
        self.tfNombre.setText(empleado.nombreEmpleado)
        self.tfApellidos.setText(empleado.apellidoEmpleado)
        self.tfEmail.setText(empleado.correoEmpleado)
        self.tfTelefono.setText(empleado.telefonoEmpleado)
        self.tfDireccion.setText(empleado.direccionResidenciaEmpleado)

    def llenar_tabla(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Código', 'Profesion'])
        profesiones = obtenerListaProfesiones()

        data = []
        for profesion in profesiones:
            data.append([profesion.codigoProfesion, profesion.nombreProfesion])

        for row in data:
            items = [QStandardItem(field) for field in row]
            for item in items:
                item.setEditable(False)
            self.model.appendRow(items)

        self.tvProfesiones.setModel(self.model)
        header = self.tvProfesiones.horizontalHeader()
        header.setStretchLastSection(True)

        self.tvProfesiones.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

    def capturar_dato_tabla(self):
        item = None
        selection_model = self.tvProfesiones.selectionModel()

        if selection_model.hasSelection():
            indexes = selection_model.selectedIndexes()
            item = self.model.itemFromIndex(indexes[0]).text()
        return item
