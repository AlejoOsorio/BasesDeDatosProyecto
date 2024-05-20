import Database
from model.Funcion import Funcion


def findById(codigoFuncion: str):
    funcion = None

    query = "SELECT * FROM funciones WHERE codigoFuncion = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoFuncion,))
    resultado = cursor.fetchone()

    if resultado:
        funcion = Funcion(
            codigoFuncion=resultado[0],
            nombreFuncion=resultado[1],
            descripcionFuncion=resultado[2],
            cargoFuncion=resultado[3]
        )
    Database.cerrarConexion(conexion)
    return funcion

def save(funcion: Funcion):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO funciones (codigoFuncion, nombreFuncion, descripcionFuncion, cargo) VALUES (?,?,?,?)",
        (funcion.codigoFuncion, funcion.nombreFuncion, funcion.descripcionFuncion, funcion.cargoFuncion))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(funcion: Funcion):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE funciones 
        SET nombreFuncion = ?, 
            descripcionFuncion = ?,
            cargo = ?  
        WHERE codigoFuncion = ?
    """, (
        funcion.nombreFuncion,
        funcion.descripcionFuncion,
        funcion.cargoFuncion,
        funcion.codigoFuncion,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoFuncion: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM funciones WHERE codigoFuncion = ?", (codigoFuncion,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM funciones")
    resultado = cursor.fetchall()

    listaFunciones = []
    for datos in resultado:
        funcion = Funcion(
            codigoFuncion=datos[0],
            nombreFuncion=datos[1],
            descripcionFuncion=datos[2],
            cargoFuncion=datos[3])
        listaFunciones.append(funcion)

    return listaFunciones