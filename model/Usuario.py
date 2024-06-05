import datetime

from model.NivelUsuario import NivelUsuario


class Usuario:
    def __init__(self, codigoUsuario: str, nombreUsuario: str, claveUsuario: str, fechaCreacionUsuario: datetime,
                 nivelUsuario: NivelUsuario):
        self.codigoUsuario = codigoUsuario
        self.nombreUsuario = nombreUsuario
        self.claveUsuario = claveUsuario
        self.fechaCreacionUsuario = fechaCreacionUsuario
        self.nivelUsuario = nivelUsuario
