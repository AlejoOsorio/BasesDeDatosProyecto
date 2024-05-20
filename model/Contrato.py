import datetime


class Contrato:
    def __init__(self, codigoContrato: str, fechaInicioContrato: datetime, fechaTerminacionContrato: datetime, empleado: str, sucursal: str, cargo:str):
        self.codigoContrato = codigoContrato
        self.fechaInicioContrato = fechaInicioContrato
        self.fechaTerminacionContrato = fechaTerminacionContrato
        self.empleado = empleado
        self.sucursal = sucursal
        self.cargo = cargo
