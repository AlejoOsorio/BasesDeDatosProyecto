import repository.ProfesionRepositoryImpl
from model.Profesion import Profesion


def crearProfesion(codigoProfesion: str, nombreProfesion: str):
    #Validar datos
    if repository.ProfesionRepositoryImpl.findById(codigoProfesion):
        raise RuntimeError("Ya hay una profesión con este codigo")

    repository.ProfesionRepositoryImpl.save(profesion=Profesion(
        codigoProfesion=codigoProfesion,
        nombreProfesion=nombreProfesion
    ))

def actualizarProfesion(codigoProfesion: str, nombreProfesion: str):
    profesion = repository.ProfesionRepositoryImpl.findById(codigoProfesion)
    if profesion is None:
        raise RuntimeError("No existe una profesión con este codigo")

    profesion.nombreProfesion=nombreProfesion

    repository.ProfesionRepositoryImpl.update(profesion)

def eliminarProfesion(codigoProfesion: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    profesion = repository.ProfesionRepositoryImpl.findById(codigoProfesion)
    if profesion is None:
        raise RuntimeError("No existe una profesión con este codigo")

    repository.ProfesionRepositoryImpl.delete(profesion.codigoProfesion)

def obtenerProfesion(codigoProfesion):
    profesion = repository.ProfesionRepositoryImpl.findById(codigoProfesion)
    if profesion is None:
        raise RuntimeError("No existe una profesión con este codigo")
    return profesion

def obtenerListaProfesiones():
    return repository.ProfesionRepositoryImpl.findAll()
