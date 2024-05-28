import Database
from model.Usuario import Usuario


def findById(codigoUsuario: str):
    usuario = None

    query = "SELECT * FROM usuarios WHERE codigoUsuario = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoUsuario,))
    resultado = cursor.fetchone()

    if resultado:
        usuario = Usuario(
            codigoUsuario=resultado[0],
            nombreUsuario=resultado[1],
            claveUsuario=resultado[2],
            fechaCreacionUsuario=resultado[3],
            nivelUsuario=resultado[4]
        )
    Database.cerrarConexion(conexion)
    return usuario

def findByNombreUsuario(nombreUsuario: str):
    usuario = None

    query = "SELECT * FROM usuarios WHERE nombreUsuario = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (nombreUsuario,))
    resultado = cursor.fetchone()

    if resultado:
        usuario = Usuario(
            codigoUsuario=resultado[0],
            nombreUsuario=resultado[1],
            claveUsuario=resultado[2],
            fechaCreacionUsuario=resultado[3],
            nivelUsuario=resultado[4]
        )
    Database.cerrarConexion(conexion)
    return usuario

def save(usuario: Usuario):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO usuarios (codigoUsuario, nombreUsuario, claveUsuario, fechaCreacionUsuario, nivelUsuario) VALUES (?,?,?,?,?)",
        (usuario.codigoUsuario, usuario.nombreUsuario, usuario.claveUsuario, usuario.fechaCreacionUsuario, usuario.nivelUsuario))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(usuario: Usuario):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE usuarios 
        SET nombreUsuario = ?, 
            claveUsuario = ?,
            fechaCreacionUsuario = ?,
            nivelUsuario = ?  
        WHERE codigoUsuario = ?
    """, (
        usuario.nombreUsuario,
        usuario.claveUsuario,
        usuario.fechaCreacionUsuario,
        usuario.nivelUsuario,
        usuario.codigoUsuario
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoUsuario: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM usuarios WHERE codigoUsuario = ?", (codigoUsuario,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultado = cursor.fetchall()

    listaUsuarios = []
    for datos in resultado:
        usuario = Usuario(
            codigoUsuario=datos[0],
            nombreUsuario=datos[1],
            claveUsuario=datos[2],
            fechaCreacionUsuario=datos[3],
            nivelUsuario=datos[4])
        listaUsuarios.append(usuario)

    return listaUsuarios