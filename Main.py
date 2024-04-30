import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from controllers.frame_empleado import Empleado
from controllers.frame_sucursal import Sucursal
from views.python_files.main_window import Ui_MainWindow


class MiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.empleado = Empleado()
        self.sucursal = Sucursal()

        self.ui.stackedWidget.addWidget(self.sucursal)
        self.ui.stackedWidget.addWidget(self.empleado)

        self.ui.actionSucursal.triggered.connect(self.abrir_frame_sucursal)
        self.ui.actionEmpleado.triggered.connect(self.abrir_frame_cliente)
        self.ui.actionSalir.triggered.connect(self.abrir_frame_principal)

    def abrir_frame_principal(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def abrir_frame_sucursal(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def abrir_frame_cliente(self):
        self.ui.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MiWindow()
    window.show()
    sys.exit(app.exec())
