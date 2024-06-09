import datetime

import repository.BitacoraRepositoryImpl
from model.Bitacora import Bitacora


def crearBitacora(codigoBitacora: str, fechaIngreso: datetime, horaIngreso: datetime, usuario: str,
                  horaSalida: datetime = None, fechaSalida: datetime = None):
    # Validar datos
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


def salirBitacora(codigo_bitacora: str):

    # Validar que la bitácora existe
    bitacora = repository.BitacoraRepositoryImpl.findById(codigo_bitacora)
    if not bitacora:
        raise RuntimeError("No hay una bitacora con este codigo para actualizar")

    # agregar los datos de salida
    bitacora.fechaSalida = datetime.date.today()
    bitacora.horaSalida = datetime.datetime.now().time()

    # Actualizar la bitácora existente
    repository.BitacoraRepositoryImpl.update(bitacora)


def obtenerBitacora(codigoBitacora):
    bitacora = repository.BitacoraRepositoryImpl.findById(codigoBitacora)
    if bitacora is None:
        raise RuntimeError("No existe una bitacora con este codigo")
    return bitacora


def obtenerListaBitacoras():
    return repository.BitacoraRepositoryImpl.findAll()


def generarCodigo():
    codigo = f"B{repository.BitacoraRepositoryImpl.sizeTable() + 1}"
    return codigo
