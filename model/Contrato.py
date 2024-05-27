import datetime


class Contrato:
    def __init__(self, codigoContrato: str, fechaContrato: datetime, fechaInicioContrato: datetime, fechaTerminacionContrato: datetime, empleado: str, sucursal: str, cargo: str):
        self.codigoContrato = codigoContrato
        self.fechaContrato = fechaContrato
        self.fechaInicioContrato = fechaInicioContrato
        self.fechaTerminacionContrato = fechaTerminacionContrato
        self.empleado = empleado
        self.sucursal = sucursal
        self.cargo = cargo
