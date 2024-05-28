from services import UsuarioServicioImpl


def login(nombreUsuario: str, claveUsuario: str):
    usuario = UsuarioServicioImpl.obtenerUsuarioPorNombre(nombreUsuario)

    if usuario.claveUsuario != claveUsuario:
        raise RuntimeError("Usuario/Clave incorrecta")

    return usuario
