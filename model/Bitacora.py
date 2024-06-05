import datetime


class Bitacora:
    def __init__(self, codigoBitacora: str, numeroIngreso: int, fechaIngreso: datetime, horaIngreso: datetime,
                 horaSalida: datetime, usuario: str, fechaSalida: datetime):
        self.codigoBitacora = codigoBitacora
        self.numeroIngreso = numeroIngreso
        self.fechaIngreso = fechaIngreso
        self.horaIngreso = horaIngreso
        self.horaSalida = horaSalida
        self.usuario = usuario
        self.fechaSalida = fechaSalida
