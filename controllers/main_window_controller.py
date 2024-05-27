from PyQt6.QtWidgets import QMainWindow

from controllers.cargo_controller import CargoController
from controllers.contrato_controller import ContratoController
from controllers.departamento_controller import DepartamentoController
from controllers.empleado_controller import EmpleadoController
from controllers.listar_sucursales_controller import ListarSucursalesController
from controllers.municipio_controller import MunicipioController
from controllers.profesion_controller import ProfesionController
from controllers.reporte_empleados_controller import ReporteEmpleadosController
from controllers.sucursal_controller import SucursalController
from controllers.tipo_municipio_controller import TipoMunicipioController
from controllers.usuario_controller import UsuarioController
from model.NivelUsuario import NivelUsuario
from utils.utils_qt import mensaje_hora, mensaje_acerca_de, abrir_calculadora
from views.python_files.frame_main_window import Ui_MainWindow


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setupUi(self)

        self.validar_tipo_usuario(usuario)

        self.empleado = EmpleadoController()
        self.sucursal = SucursalController()
        self.cargo = CargoController()
        self.municipio = MunicipioController()
        self.profesion = ProfesionController()
        self.contrato = ContratoController()
        self.departamento = DepartamentoController()
        self.tipo_municipio = TipoMunicipioController()
        self.usuario = UsuarioController()
        self.filtroSucursales = ListarSucursalesController()
        self.reporteEmpleados = ReporteEmpleadosController()

        self.stackedWidget.addWidget(self.sucursal)
        self.stackedWidget.addWidget(self.empleado)
        self.stackedWidget.addWidget(self.cargo)
        self.stackedWidget.addWidget(self.municipio)
        self.stackedWidget.addWidget(self.profesion)
        self.stackedWidget.addWidget(self.contrato)
        self.stackedWidget.addWidget(self.departamento)
        self.stackedWidget.addWidget(self.tipo_municipio)
        self.stackedWidget.addWidget(self.usuario)
        self.stackedWidget.addWidget(self.filtroSucursales)
        self.stackedWidget.addWidget(self.reporteEmpleados)

        self.actionVentana_Principal.triggered.connect(lambda: self.abrir_frame(0))
        self.actionSucursal.triggered.connect(lambda: self.abrir_frame(1))
        self.actionEmpleado.triggered.connect(lambda: self.abrir_frame(2))
        self.actionCargo.triggered.connect(lambda: self.abrir_frame(3))
        self.actionMunicipio.triggered.connect(lambda: self.abrir_frame(4))
        self.actionProfesion.triggered.connect(lambda: self.abrir_frame(5))
        self.actionContrato.triggered.connect(lambda: self.abrir_frame(6))
        self.actionDepartamento.triggered.connect(lambda: self.abrir_frame(7))
        self.actionTipo_Municipio.triggered.connect(lambda: self.abrir_frame(8))
        self.actionUsuario.triggered.connect(lambda: self.abrir_frame(9))
        self.actionListar_sucursales.triggered.connect(lambda: self.abrir_frame(10))
        self.actionInforme_empleados.triggered.connect(lambda: self.abrir_frame(11))
        self.actionFecha_y_hora_actual.triggered.connect(mensaje_hora)
        self.actionAcerca_de.triggered.connect(mensaje_acerca_de)
        self.actionCalculadora.triggered.connect(abrir_calculadora)

    def abrir_frame(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def validar_tipo_usuario(self, usuario):
        if usuario.nivel == NivelUsuario.PRINCIPAL:
            self.bloquer_principal()
        elif usuario.nivel == NivelUsuario.ESPORADICO:
            self.bloquer_esporadicos()
        elif usuario.nivel == NivelUsuario.PARAMETRICO:
            self.bloquer_parametricos()

    def bloquer_parametricos(self):
        self.actionDepartamento.setDisabled(True)
        self.actionTipo_Municipio.setDisabled(True)
        self.actionMunicipio.setDisabled(True)
        self.actionSucursal.setDisabled(True)
        self.actionCargo.setDisabled(True)
        self.actionProfesion.setDisabled(True)
        self.actionEmpleado.setDisabled(True)

    def bloquer_esporadicos(self):
        self.actionDepartamento.setDisabled(True)
        self.actionTipo_Municipio.setDisabled(True)
        self.actionMunicipio.setDisabled(True)
        self.actionSucursal.setDisabled(True)

    def bloquer_principal(self):
        pass