import UsuarioServicioImpl

def login(nombreUsuario: str, claveUsuario: str):
    usuario = UsuarioServicioImpl.obtenerUsuario(nombreUsuario)

    if usuario.claveUsuario != claveUsuario:
        raise RuntimeError("Usuario/Clave incorrecta")



    return True