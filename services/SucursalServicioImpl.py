import repository.SucursalRepositoryImpl
import services.MunicipioServicioImpl
from model.Sucursal import Sucursal


def crearSucursal(codigoSucursal: str, nombreSucursal: str, presupuestoAnual: float, direccionSucursal: str, telefono: str, municipio: str):
    #Validar datos
    if repository.SucursalRepositoryImpl.findById(codigoSucursal):
        raise RuntimeError("Ya hay una sucursal con este codigo")

    #Obteniendo el municipio valida si el municipio existe o no
    services.MunicipioServicioImpl.obtenerMunicipio(municipio)


    repository.SucursalRepositoryImpl.save(sucursal=Sucursal(
        codigoSucursal=codigoSucursal,
        nombreSucursal=nombreSucursal,
        presupuestoAnual=presupuestoAnual,
        direccionSucursal=direccionSucursal,
        telefono=telefono,
        municipio=municipio
    ))

def actualizarSucursal(codigoSucursal: str, nombreSucursal: str, presupuestoAnual: float, direccionSucursal: str, telefono: str, municipio: str):
    sucursal = repository.SucursalRepositoryImpl.findById(codigoSucursal)
    if sucursal is None:
        raise RuntimeError("No existe una sucursal con este codigo")

    # Obteniendo el municipio valida si el municipio existe o no
    services.MunicipioServicioImpl.obtenerMunicipio(municipio)


    sucursal.nombreSucursal=nombreSucursal
    sucursal.presupuestoAnual=presupuestoAnual
    sucursal.direccionSucursal=direccionSucursal
    sucursal.telefono=telefono
    sucursal.municipio=municipio

    repository.SucursalRepositoryImpl.update(sucursal)

def eliminarSucursal(codigoSucursal: str):
    # Pongo esto porque no tira error si uno pone un id que no existe
    sucursal = repository.SucursalRepositoryImpl.findById(codigoSucursal)
    if sucursal is None:
        raise RuntimeError("No existe una sucursal con este codigo")

    repository.SucursalRepositoryImpl.delete(sucursal.codigoSucursal)

def obtenerSucursal(codigoSucursal):
    sucursal = repository.SucursalRepositoryImpl.findById(codigoSucursal)
    if sucursal is None:
        raise RuntimeError("No existe una sucursal con este codigo")
    return sucursal

def obtenerListaSucursal():
    return repository.SucursalRepositoryImpl.findAll()
