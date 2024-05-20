import repository.DepartamentoRepositoryImpl
from model.Departamento import Departamento

def crearDepartamento(codigoDepartamento: str, nombreDepartamento: str, poblacionDepartamento: int):
    #Validar datos
    if repository.DepartamentoRepositoryImpl.findById(codigoDepartamento):
        raise RuntimeError("Ya hay un departamento con este codigo")

    repository.DepartamentoRepositoryImpl.save(departamento=Departamento(
        codigoDepartamento=codigoDepartamento,
        nombreDepartamento=nombreDepartamento,
        poblacionDepartamento=poblacionDepartamento,
    ))

def actualizarDepartamento(codigoDepartamento: str, nombreDepartamento: str, poblacionDepartamento: int):
    departamento = repository.DepartamentoRepositoryImpl.findById(codigoDepartamento)
    if departamento is None:
        raise RuntimeError("No existe un departamento con este codigo")

    departamento.nombreDepartamento=nombreDepartamento
    departamento.poblacionDepartamento=poblacionDepartamento

    repository.DepartamentoRepositoryImpl.update(departamento)

def eliminarDepartamento(codigoDepartamento: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    departamento = repository.DepartamentoRepositoryImpl.findById(codigoDepartamento)
    if departamento is None:
        raise RuntimeError("No existe un departamento con este codigo")

    repository.DepartamentoRepositoryImpl.delete(departamento.codigoDepartamento)

def obtenerDepartamento(codigoDepartamento):
    departamento = repository.DepartamentoRepositoryImpl.findById(codigoDepartamento)
    if departamento is None:
        raise RuntimeError("No existe un departamento con este codigo")
    return departamento

def obtenerListaCargos():
    return repository.DepartamentoRepositoryImpl.findAll()
