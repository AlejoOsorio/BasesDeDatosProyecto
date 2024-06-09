from PyQt6 import QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QTableView

from services.BitacoraServicioImpl import obtenerListaBitacoras
from views.python_files.frame_bitacora import Ui_Frame


class BitacoraController(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_tabla()

    def llenar_tabla(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Código', 'Numero', 'Fecha Ingreso', 'Hora Ingres', 'Hora Salida', 'Usuario', 'Fecha salida'])
        bitacoras = obtenerListaBitacoras()

        data = [[bitacora.codigoBitacora, bitacora.numeroIngreso, bitacora.fechaIngreso, bitacora.horaIngreso,
                 bitacora.horaSalida, bitacora.usuario, bitacora.fechaSalida] for bitacora in bitacoras]

        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            for item in items:
                item.setEditable(False)
            self.model.appendRow(items)

        self.tvBitacora.setModel(self.model)

        header = self.tvBitacora.horizontalHeader()
        header.setStretchLastSection(True)

        self.tvBitacora.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
