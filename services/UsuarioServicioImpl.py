import datetime

import repository.UsuarioRepositoryImpl
from model.NivelUsuario import NivelUsuario
from model.Usuario import Usuario


def crearUsuario(codigoUsuario: str, nombreUsuario: str, claveUsuario: str, nivelUsuario: NivelUsuario):
    #Validar datos
    if repository.UsuarioRepositoryImpl.findById(codigoUsuario):
        raise RuntimeError("Ya hay un usuario con este codigo")
    if repository.UsuarioRepositoryImpl.findByNombreUsuario(nombreUsuario):
        raise RuntimeError("Ya hay un usuario con este nombre de usuario")

    repository.UsuarioRepositoryImpl.save(usuario=Usuario(
        codigoUsuario=codigoUsuario,
        nombreUsuario=nombreUsuario,
        claveUsuario=claveUsuario,
        fechaCreacionUsuario=datetime.date.today(),
        nivelUsuario=nivelUsuario
    ))

def actualizarUsuario(codigoUsuario: str, nombreUsuario: str, claveUsuario: str, nivelUsuario: NivelUsuario):
    usuario = repository.UsuarioRepositoryImpl.findById(codigoUsuario)
    if usuario is None:
        raise RuntimeError("No existe un usuario con este codigo")

    usuario.nombreUsuario=nombreUsuario
    usuario.claveUsuario=claveUsuario
    usuario.nivelUsuario=nivelUsuario

    repository.UsuarioRepositoryImpl.update(usuario)

def eliminarUsuario(codigoUsuario: str):
    ##Pongo esto porque no tira error si uno pone un id que no existe
    usuario = repository.UsuarioRepositoryImpl.findById(codigoUsuario)
    if usuario is None:
        raise RuntimeError("No existe un usuario con este codigo")

    repository.UsuarioRepositoryImpl.delete(usuario.codigoUsuario)

def obtenerUsuario(codigoUsuario):
    usuario = repository.UsuarioRepositoryImpl.findById(codigoUsuario)
    if usuario is None:
        raise RuntimeError("No existe un usuario con este codigo")
    return usuario

def obtenerUsuarioPorNombre(nombreUsuario):
    usuario = repository.UsuarioRepositoryImpl.findByNombreUsuario(nombreUsuario)
    if usuario is None:
        raise RuntimeError("No existe un usuario con este codigo")
    return usuario

def obtenerListaUsuarios():
    return repository.UsuarioRepositoryImpl.findAll()
