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
        self.login = None
        self.setupUi(self)
        self.usuario = usuario
        self.frames = []

        self.validar_tipo_usuario(self.usuario)
        self.cargar_frames()

    def cargar_frames(self):
        self.frames = [SucursalController(), EmpleadoController(), CargoController(), MunicipioController(),
                       ProfesionController(), ContratoController(), DepartamentoController(), TipoMunicipioController(),
                       UsuarioController(), ListarSucursalesController(self.usuario.nivelUsuario),
                       ReporteEmpleadosController(self.usuario.nivelUsuario)]

        [self.stackedWidget.addWidget(frame) for frame in self.frames]

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
        self.actionLogout.triggered.connect(self.logout)
        self.actionFecha_y_hora_actual.triggered.connect(mensaje_hora)
        self.actionAcerca_de.triggered.connect(mensaje_acerca_de)
        self.actionCalculadora.triggered.connect(abrir_calculadora)

    def abrir_frame(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def validar_tipo_usuario(self, usuario):
        if usuario.nivelUsuario == NivelUsuario.PRINCIPAL:
            self.bloquer_principal()
        elif usuario.nivelUsuario == NivelUsuario.ESPORADICO:
            self.bloquer_esporadicos()
        elif usuario.nivelUsuario == NivelUsuario.PARAMETRICO:
            self.bloquer_parametricos()

    def bloquer_principal(self):
        pass

    def bloquer_parametricos(self):
        self.actionDepartamento.setDisabled(True)
        self.actionTipo_Municipio.setDisabled(True)
        self.actionMunicipio.setDisabled(True)
        self.actionSucursal.setDisabled(True)
        self.actionCargo.setDisabled(True)
        self.actionProfesion.setDisabled(True)
        self.actionEmpleado.setDisabled(True)
        self.actionContrato.setDisabled(True)
        self.actionUsuario.setDisabled(True)
        self.actionBitacora.setDisabled(True)

    def bloquer_esporadicos(self):
        self.bloquer_parametricos()

    def logout(self):
        from controllers.login_controller import LogInController
        self.login = LogInController()
        self.close()
        self.login.show()
