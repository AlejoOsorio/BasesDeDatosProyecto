import datetime
from subprocess import call

from PyQt6.QtWidgets import QMessageBox


def mensaje_error(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.exec()


def mensaje_informacion(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(message)
    msg.setWindowTitle("Information")
    msg.exec()


def mensaje_hora():
    msg = QMessageBox()
    fecha = (datetime.datetime.now())
    fomateado = fecha.strftime("%H:%M:%S - %d/%m/%Y")
    msg.setText(fomateado)
    msg.setWindowTitle("Fecha y hora actual")
    msg.exec()


def mensaje_acerca_de():
    msg = QMessageBox()
    msg.setText('''
    UniBanco V1.0
    Creado por:
    Sergio Alejandro Patiño Osorio
    Juan Camilo Cortés Dávila
    Sebastian Jaramillo Cardona''')
    msg.setWindowTitle("Acerca de")
    msg.exec()


def abrir_calculadora():
    call(["calc.exe"])
