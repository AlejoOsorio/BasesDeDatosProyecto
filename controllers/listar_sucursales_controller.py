from itertools import zip_longest
from tkinter import filedialog

from PyQt6 import QtWidgets
from PyQt6.QtCore import QVariant
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QButtonGroup, QRadioButton, QHBoxLayout, QWidget, \
    QVBoxLayout, QCheckBox, QLabel, QLineEdit, QWidget as EmptyWidget

from model.NivelUsuario import NivelUsuario
from repository.ConsultasImpl import consulta_sucursales_nivel_principal, consulta_sucursales_nivel_esporadico, \
    consulta_sucursales_nivel_parametrico
from utils.reporte import Report
from utils.utils_qt import mensaje_error
from views.python_files.frame_listar_sucursales import Ui_Frame


class ListarSucursalesController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, nivel_usuario: NivelUsuario, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.campos_filtros = QVBoxLayout()
        self.nivel_usuario = nivel_usuario
        self.field_checkboxes = []
        self.datos_informe = []
        self.campos_filtro = {}
        self.btnGenerarInforme.clicked.connect(self.generar_reporte)
        self.btnVistaPrevia.clicked.connect(self.llenar_tabla)

        # Generar interfaz en tiempo real dependiendo del tipo de usuario
        self.crear_check_box()
        self.crear_filtros()

    def buscar_datos(self):

        if self.radio_custom_fields.isChecked():
            campos_seleccionados = [cb.property("campo") for cb in self.field_checkboxes if cb.isChecked()]
            titulos = [cb.text() for cb in self.field_checkboxes if cb.isChecked()]
        else:
            campos_seleccionados = [cb.property("campo") for cb in self.field_checkboxes]
            titulos = [cb.text() for cb in self.field_checkboxes]

        if len(campos_seleccionados) == 0:
            mensaje_error("Es necesario que seleccione un campo")
            return None, None

        if self.nivel_usuario == NivelUsuario.PRINCIPAL:
            municipio = self.campos_filtro["tfMunicipio"].text().strip()
            departamento = self.campos_filtro["tfDepartamento"].text().strip()
            nombre_sucursal = self.campos_filtro["tfNombreSucursal"].text().strip()
            poblacion_municipio = self.campos_filtro["tfPoblacionMunicipio"].text().strip()
            prioridad = self.campos_filtro["tfNivelPrioridad"].text().strip()
            datos = consulta_sucursales_nivel_principal(", ".join(campos_seleccionados), poblacion_municipio, prioridad,
                                                        municipio, departamento, nombre_sucursal)
        elif self.nivel_usuario == NivelUsuario.PARAMETRICO:
            nombre_sucursal = self.campos_filtro["tfNombreSucursal"].text().strip()
            poblacion_departamento = self.campos_filtro["tfPoblacionDepartamento"].text().strip()
            datos = consulta_sucursales_nivel_parametrico(", ".join(campos_seleccionados), poblacion_departamento,
                                                          nombre_sucursal)
        else:
            municipio = self.campos_filtro["tfMunicipio"].text().strip()
            departamento = self.campos_filtro["tfDepartamento"].text().strip()
            datos = consulta_sucursales_nivel_esporadico(", ".join(campos_seleccionados), municipio, departamento)

        return datos, titulos

    def llenar_tabla(self):
        self.datos_informe, titulos = self.buscar_datos()

        if self.datos_informe is None or titulos is None:
            return

        if self.datos_informe:
            self.twEmpleados.setColumnCount(len(self.datos_informe[0]))
            self.twEmpleados.setRowCount(len(self.datos_informe))
            self.twEmpleados.setHorizontalHeaderLabels(titulos)

            for row_idx, row_data in enumerate(self.datos_informe):
                for col_idx, value in enumerate(row_data):
                    self.twEmpleados.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            self.twEmpleados.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        else:
            self.twEmpleados.setColumnCount(0)
            self.twEmpleados.setRowCount(0)

    def crear_check_box(self):
        self.radio_group = QButtonGroup(self)
        self.radio_all_fields = QRadioButton("Todos los campos")
        self.radio_custom_fields = QRadioButton("Campos personalizados")

        self.radio_group.addButton(self.radio_all_fields)
        self.radio_group.addButton(self.radio_custom_fields)

        self.radio_layout = QHBoxLayout()
        self.radio_layout.addWidget(self.radio_all_fields)
        self.radio_layout.addWidget(self.radio_custom_fields)
        self.campos_filtros.addLayout(self.radio_layout)

        self.radio_all_fields.setChecked(True)

        self.fields_widget = QWidget()
        fields_layout = QVBoxLayout(self.fields_widget)
        fields = self.fields_usuario(self.nivel_usuario)

        it = iter(fields.items())
        for pair in zip_longest(it, it, it, it, it, it):
            linea = QHBoxLayout()
            for key, campo in filter(None, pair):
                checkbox = QCheckBox(key)
                checkbox.setProperty("campo", QVariant(campo))
                self.field_checkboxes.append(checkbox)
                linea.addWidget(checkbox)
            while len(linea) < 6:
                empty = EmptyWidget()
                linea.addWidget(empty)
            fields_layout.addLayout(linea)
        self.campos_filtros.addWidget(self.fields_widget)
        self.verticalLayout.insertLayout(2, self.campos_filtros)
        self.fields_widget.setVisible(False)

        self.radio_custom_fields.toggled.connect(self.toggle_fields_selection)

    def crear_filtros(self):
        filtros = self.filtros_usuario(self.nivel_usuario)

        it = iter(filtros.items())
        for pair in zip_longest(it, it, it, it):
            linea = QHBoxLayout()
            for key, filtro in filter(None, pair):
                vertical = QVBoxLayout()
                campo = filtro[1]
                label = QLabel(filtro[0])
                campo.setMaximumWidth(100)
                vertical.addWidget(label)
                vertical.addWidget(campo)
                linea.addLayout(vertical)
                self.campos_filtro[key] = campo
            while len(linea) < 4:
                empty = EmptyWidget()
                empty.setMaximumWidth(100)
                linea.addWidget(empty)

            self.campos_filtros.addLayout(linea)

    def toggle_fields_selection(self):
        self.fields_widget.setVisible(self.radio_custom_fields.isChecked())

    def filtros_usuario(self, nivel_usuario: NivelUsuario):
        if nivel_usuario == NivelUsuario.PRINCIPAL:
            filtros = {
                "tfNombreSucursal": ["Nombre Sucursal", QLineEdit()],
                "tfPoblacionMunicipio": ["Población Municipio", QLineEdit()],
                "tfNivelPrioridad": ["Prioridad Municipio", QLineEdit()],
                "tfMunicipio": ["Municipio", QLineEdit()],
                "tfDepartamento": ["Departamento", QLineEdit()]
            }
        elif nivel_usuario == NivelUsuario.PARAMETRICO:
            filtros = {
                "tfNombreSucursal": ["Nombre Sucursal", QLineEdit()],
                "tfPoblacionDepartamento": ["Población Departamento", QLineEdit()]
            }

        else:
            filtros = {
                "tfMunicipio": ["Municipio", QLineEdit()],
                "tfDepartamento": ["Departamento", QLineEdit()],
            }

        return filtros

    def fields_usuario(self, nivel_usuario: NivelUsuario):
        if nivel_usuario == NivelUsuario.PRINCIPAL:
            campos = {
                "Nombre Sucursal": "s.nombreSucursal",
                "Presupuesto": "s.presupuestoAnualSucursal",
                "Dirección": "s.direccionSucursal",
                "Teléfono": "s.telefonoSucursal",
                "Municipio": "m.nombreMunicipio",
                "Población Municipio": "m.poblacion",
                "Prioridad Municipio": "p.nombrePrioridad",
                "Departamento": "d.nombreDepartamento",
                "Población Departamento": "d.poblacion"
            }
        elif nivel_usuario == NivelUsuario.PARAMETRICO:
            campos = {
                "Nombre Sucursal": "s.nombreSucursal",
                "Dirección": "s.direccionSucursal",
                "Teléfono": "s.telefonoSucursal",
                "Municipio": "m.nombreMunicipio",
                "Departamento": "d.nombreDepartamento",
                "Población Departamento": "d.poblacion"
            }
        else:
            campos = {
                "Nombre Sucursal": "s.nombreSucursal",
                "Dirección": "s.direccionSucursal",
                "Teléfono": "s.telefonoSucursal",
                "Municipio": "m.nombreMunicipio",
                "Departamento": "d.nombreDepartamento",
            }

        return campos

    def generar_reporte(self):
        try:
            ruta = filedialog.askdirectory()
            empleados, headers = self.buscar_datos()

            if empleados is None or headers is None:
                return

            Report(f"{ruta}/reporte-empleados.pdf", headers, empleados, 'Informe Sucursales')
        except Exception as e:
            print(e)
