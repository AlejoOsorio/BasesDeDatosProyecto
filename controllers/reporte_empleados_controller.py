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

            headers = ["Codigo", "Cedula", "Nombre", "Apellido", "Direccion", "Telefono", "Correo"]
            body = tuple((empleado.codigoEmpleado, empleado.cedulaEmpleado, empleado.nombreEmpleado,
                          empleado.apellidoEmpleado, empleado.direccionResidenciaEmpleado, empleado.telefonoEmpleado,
                          empleado.correoEmpleado) for empleado in empleados)

            Report(f"{ruta}/reporte-empleados.pdf", headers, body)
        except Exception as e:
            print(e)
