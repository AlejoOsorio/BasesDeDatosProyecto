import repository.CargoRepositoryImpl
from model.Cargo import Cargo


def crearCargo(codigoCargo: str, nombreCargo: str, salarioCargo: str):
    #Validar datos
    if repository.CargoRepositoryImpl.findById(codigoCargo):
        raise RuntimeError("Ya hay un cargo con este codigo")

    repository.CargoRepositoryImpl.save(cargo=Cargo(
        codigoCargo=codigoCargo,
        nombreCargo=nombreCargo,
        salarioCargo=salarioCargo,
    ))

def actualizarCargo(codigoCargo: str, nombreCargo: str, salarioCargo: float):
    cargo = repository.CargoRepositoryImpl.findById(codigoCargo)
    if cargo is None:
        raise RuntimeError("No existe un cargo con este codigo")

    cargo.nombreCargo=nombreCargo
    cargo.salarioCargo=salarioCargo

    repository.CargoRepositoryImpl.update(cargo)

def eliminarCargo(codigoCargo: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    cargo = repository.CargoRepositoryImpl.findById(codigoCargo)
    if cargo is None:
        raise RuntimeError("No existe un cargo con este codigo")

    repository.CargoRepositoryImpl.delete(cargo.codigoCargo)

def obtenerCargo(codigoCargo):
    cargo = repository.CargoRepositoryImpl.findById(codigoCargo)
    if cargo is None:
        raise RuntimeError("No existe un cargo con este codigo")
    return cargo

def obtenerListaCargos():
    return repository.CargoRepositoryImpl.findAll()
