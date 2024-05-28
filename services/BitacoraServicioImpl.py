import datetime

import repository.BitacoraRepositoryImpl
from model.Bitacora import Bitacora


def crearBitacora(codigoBitacora: str, fechaIngreso: datetime, horaIngreso: datetime,
                 horaSalida: datetime, usuario: str, fechaSalida: datetime):
    #Validar datos
    if repository.BitacoraRepositoryImpl.findById(codigoBitacora):
        raise RuntimeError("Ya hay una bitacora con este codigo")

    repository.BitacoraRepositoryImpl.save(bitacora=Bitacora(
        codigoBitacora=codigoBitacora,
        numeroIngreso=0,
        fechaIngreso=fechaIngreso,
        horaIngreso=horaIngreso,
        horaSalida=horaSalida,
        usuario=usuario,
        fechaSalida=fechaSalida
    ))

def obtenerBitacora(codigoBitacora):
    bitacora = repository.BitacoraRepositoryImpl.findById(codigoBitacora)
    if bitacora is None:
        raise RuntimeError("No existe una bitacora con este codigo")
    return bitacora

def obtenerListaBitacoras():
    return repository.BitacoraRepositoryImpl.findAll()
