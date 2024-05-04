from PyQt6.QtWidgets import QMainWindow

from controllers.cargo_controller import CargoController
from controllers.contrato_controller import ContratoController
from controllers.departamento_controller import DepartamentoController
from controllers.empleado_controller import EmpleadoController
from controllers.municipio_controller import MunicipioController
from controllers.profesion_controller import ProfesionController
from controllers.sucursal_controller import SucursalController
from controllers.tipo_municipio_controller import TipoMunicipioController
from views.python_files.frame_main_window import Ui_MainWindow


class MainWindowController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.empleado = EmpleadoController()
        self.sucursal = SucursalController()
        self.cargo = CargoController()
        self.municipio = MunicipioController()
        self.profesion = ProfesionController()
        self.contrato = ContratoController()
        self.departamento = DepartamentoController()
        self.tipo_municipio = TipoMunicipioController()

        self.stackedWidget.addWidget(self.sucursal)
        self.stackedWidget.addWidget(self.empleado)
        self.stackedWidget.addWidget(self.cargo)
        self.stackedWidget.addWidget(self.municipio)
        self.stackedWidget.addWidget(self.profesion)
        self.stackedWidget.addWidget(self.contrato)
        self.stackedWidget.addWidget(self.departamento)
        self.stackedWidget.addWidget(self.tipo_municipio)

        self.actionSalir.triggered.connect(lambda: self.abrir_frame(0))
        self.actionSucursal.triggered.connect(lambda: self.abrir_frame(1))
        self.actionEmpleado.triggered.connect(lambda: self.abrir_frame(2))
        self.actionCargo.triggered.connect(lambda: self.abrir_frame(3))
        self.actionMunicipio.triggered.connect(lambda: self.abrir_frame(4))
        self.actionProfesion.triggered.connect(lambda: self.abrir_frame(5))
        self.actionContrato.triggered.connect(lambda: self.abrir_frame(6))
        self.actionDepartamento.triggered.connect(lambda: self.abrir_frame(7))
        self.actionTipo_Municipio.triggered.connect(lambda: self.abrir_frame(8))

    def abrir_frame(self, index):
        self.stackedWidget.setCurrentIndex(index)
