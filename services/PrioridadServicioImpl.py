import repository.PrioridadRepositoryImpl
from model.Prioridad import Prioridad


def crearPrioridad(codigoPrioridad: str, nombrePrioridad: str):
    #Validar datos
    if repository.PrioridadRepositoryImpl.findById(codigoPrioridad):
        raise RuntimeError("Ya hay una prioridad con este codigo")

    repository.PrioridadRepositoryImpl.save(prioridad=Prioridad(
        codigoPrioridad=codigoPrioridad,
        nombrePrioridad=nombrePrioridad
        ))

def actualizarPrioridad(codigoPrioridad: str, nombrePrioridad: str):
    prioridad = repository.PrioridadRepositoryImpl.findById(codigoPrioridad)
    if prioridad is None:
        raise RuntimeError("No existe una prioridad con este codigo")

    prioridad.nombrePrioridad=nombrePrioridad

    repository.PrioridadRepositoryImpl.update(prioridad)

def eliminarPrioridad(codigoPrioridad: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    prioridad = repository.PrioridadRepositoryImpl.findById(codigoPrioridad)
    if prioridad is None:
        raise RuntimeError("No existe una prioridad con este codigo")

    repository.PrioridadRepositoryImpl.delete(prioridad.codigoPrioridad)

def obtenerPrioridad(codigoProridad: str):
    prioridad = repository.PrioridadRepositoryImpl.findById(codigoProridad)
    if prioridad is None:
        raise RuntimeError("No existe una prioridad con este codigo")
    return prioridad

def obtenerListaPrioridades():
    return repository.PrioridadRepositoryImpl.findAll()
