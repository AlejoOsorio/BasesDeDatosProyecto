import datetime

import repository.ContratoRepositoryImpl
import services.EmpleadoServicioImpl as EmpleadoServicioImpl
import services.SucursalServicioImpl as SucursalServicioImpl
import services.CargoServicioImpl as CargoServicioImpl
from model.Contrato import Contrato


def crearContrato(codigoContrato: str, fechaInicioContrato: datetime, fechaTerminacionContrato: datetime, empleado: str,
                  sucursal: str, cargo: str):
    # Validar datos
    if repository.ContratoRepositoryImpl.findById(codigoContrato):
        raise RuntimeError("Ya hay un contrato con este codigo")

    # Estas lineas validan si existen en la base de datos
    EmpleadoServicioImpl.obtenerEmpleado(empleado)
    SucursalServicioImpl.obtenerSucursal(sucursal)
    CargoServicioImpl.obtenerCargo(cargo)

    repository.ContratoRepositoryImpl.save(contrato=Contrato(
        codigoContrato=codigoContrato,
        fechaContrato=datetime.date.today(),
        fechaInicioContrato=fechaInicioContrato,
        fechaTerminacionContrato=fechaTerminacionContrato,
        empleado=empleado,
        sucursal=sucursal,
        cargo=cargo
    ))


def actualizarContrato(codigoContrato: str, fechaContrato: datetime, fechaInicioContrato: datetime, fechaTerminacionContrato: datetime,
                       empleado: str, sucursal: str, cargo: str):
    contrato = repository.ContratoRepositoryImpl.findById(codigoContrato)
    if contrato is None:
        raise RuntimeError("No existe un cargo con este codigo")

    # Estas lineas validan si existen en la base de datos
    EmpleadoServicioImpl.obtenerEmpleado(empleado)
    SucursalServicioImpl.obtenerSucursal(sucursal)
    CargoServicioImpl.obtenerCargo(cargo)

    contrato.fechaContrato = fechaContrato
    contrato.fechaInicioContrato = fechaInicioContrato
    contrato.fechaTerminacionContrato = fechaTerminacionContrato
    contrato.empleado = empleado
    contrato.sucursal = sucursal
    contrato.cargo = cargo

    repository.ContratoRepositoryImpl.update(contrato)


def eliminarContrato(codigoContrato: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    contrato = repository.ContratoRepositoryImpl.findById(codigoContrato)
    if contrato is None:
        raise RuntimeError("No existe un contrato con este codigo")

    repository.ContratoRepositoryImpl.delete(contrato.codigoContrato)


def obtenerContrato(codigoContrato):
    contrato = repository.ContratoRepositoryImpl.findById(codigoContrato)
    if contrato is None:
        raise RuntimeError("No existe un contrato con este codigo")
    return contrato


def obtenerListaContratos():
    return repository.ContratoRepositoryImpl.findAll()
