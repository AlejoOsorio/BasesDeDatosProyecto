import repository.MunicipioRepositoryImpl
import services.DepartamentoServicioImpl as DepartamentoServicioImpl
import services.PrioridadServicioImpl as PrioridadServicioImpl
from model.Municipio import Municipio


def crearMunicipio(codigoMunicipio: str, nombreMunicipio: str, prioridad: str, departamento: str, poblacionMunicipio: int):
    #Validar datos
    if repository.MunicipioRepositoryImpl.findById(codigoMunicipio):
        raise RuntimeError("Ya hay un municipio con este codigo")

    #Esto verifica si existe la prioridad
    PrioridadServicioImpl.obtenerPrioridad(prioridad)
    #Esto verifica si existe el departamento
    DepartamentoServicioImpl.obtenerDepartamento(departamento)

    repository.MunicipioRepositoryImpl.save(municipo=Municipio(
        codigoMunicipio=codigoMunicipio,
        nombreMunicipio=nombreMunicipio,
        prioridad=prioridad,
        departamento=departamento,
        poblacionMunicipio=poblacionMunicipio
    ))

def actualizarMunicipio(codigoMunicipio: str, nombreMunicipio: str, prioridad: str, departamento: str, poblacionMunicipio: int):
    municipio = repository.MunicipioRepositoryImpl.findById(codigoMunicipio)
    if municipio is None:
        raise RuntimeError("No existe un municipio con este codigo")

    #Esto verifica si existe la prioridad
    PrioridadServicioImpl.obtenerPrioridad(prioridad)
    #Esto verifica si existe el departamento
    DepartamentoServicioImpl.obtenerDepartamento(departamento)

    municipio.nombreMunicipio=nombreMunicipio
    municipio.prioridad=prioridad
    municipio.departamento=departamento
    municipio.poblacionMunicipio=poblacionMunicipio

    repository.MunicipioRepositoryImpl.update(municipio)

def eliminarMunicipio(codigoMunicipio: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    municipio = repository.MunicipioRepositoryImpl.findById(codigoMunicipio)
    if municipio is None:
        raise RuntimeError("No existe un municipio con este codigo")

    repository.MunicipioRepositoryImpl.delete(municipio.codigoMunicipio)

def obtenerMunicipio(codigoMunicipio):
    municipio = repository.MunicipioRepositoryImpl.findById(codigoMunicipio)
    if municipio is None:
        raise RuntimeError("No existe un municipio con este codigo")
    return municipio

def obtenerListaMunicipios():
    return repository.MunicipioRepositoryImpl.findAll()
