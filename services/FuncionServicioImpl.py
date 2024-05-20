import repository.FuncionRepositoryImpl
import services.CargoServicioImpl as CargoServicioImpl
from model.Funcion import Funcion


def crearFuncion(codigoFuncion: str, nombreFuncion: str, descripcionFuncion: str, cargoFuncion: str):
    #Validar datos
    if repository.FuncionRepositoryImpl.findById(codigoFuncion):
        raise RuntimeError("Ya hay una función con este codigo")

    #Con esto se valida si el cargo existe
    CargoServicioImpl.obtenerCargo(cargoFuncion)

    repository.FuncionRepositoryImpl.save(funcion=Funcion(
        codigoFuncion=codigoFuncion,
        nombreFuncion=nombreFuncion,
        descripcionFuncion=descripcionFuncion,
        cargoFuncion=cargoFuncion
    ))

def actualizarFuncion(codigoFuncion: str, nombreFuncion: str, descripcionFuncion: str, cargoFuncion: str):
    funcion = repository.FuncionRepositoryImpl.findById(codigoFuncion)
    if funcion is None:
        raise RuntimeError("No existe una función con este codigo")

    #Con esto se valida si el cargo existe
    CargoServicioImpl.obtenerCargo(cargoFuncion)

    funcion.nombreFuncion=nombreFuncion
    funcion.descripcionFuncion=descripcionFuncion
    funcion.cargoFuncion=cargoFuncion

    repository.FuncionRepositoryImpl.update(funcion)

def eliminarFuncion(codigoFuncion: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    funcion = repository.FuncionRepositoryImpl.findById(codigoFuncion)
    if funcion is None:
        raise RuntimeError("No existe una función con este codigo")

    repository.FuncionRepositoryImpl.delete(funcion.codigoFuncion)

def obtenerFuncion(codigoFuncion):
    funcion = repository.FuncionRepositoryImpl.findById(codigoFuncion)
    if funcion is None:
        raise RuntimeError("No existe una función con este codigo")
    return funcion

def obtenerListaFunciones():
    return repository.FuncionRepositoryImpl.findAll()
