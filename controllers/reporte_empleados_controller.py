from tkinter import filedialog

from PyQt6 import QtWidgets

from services.EmpleadoServicioImpl import obtenerListaEmpleados
from utils.reporte import Report
from views.python_files.frame_reporte_empleados import Ui_Frame


class ReporteEmpleadosController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generar_reporte)

    def generar_reporte(self):
        try:
            ruta = filedialog.askdirectory()
            empleados = obtenerListaEmpleados()

            tupla_empleados = tuple((empleado.nombreEmpleado, empleado.cedulaEmpleado, empleado.telefonoEmpleado) for empleado in empleados)

            creador = Report(f"{ruta}/reporte-empleados.pdf", tupla_empleados)
        except Exception as e:
            print(e)

