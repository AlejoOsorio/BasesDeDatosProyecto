import Database
from model.Profesion import Profesion


def findById(codigoProfesion: str):
    profesion = None

    query = "SELECT * FROM profesiones WHERE codigoProfesion = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoProfesion,))
    resultado = cursor.fetchone()

    if resultado:
        profesion = Profesion(
            codigoProfesion=resultado[0],
            nombreProfesion=resultado[1]
        )
    Database.cerrarConexion(conexion)
    return profesion

def save(profesion: Profesion):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO profesiones (codigoProfesion, nombreProfesion) VALUES (?,?)",
        (profesion.codigoProfesion, profesion.nombreProfesion))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(profesion: Profesion):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE profesiones 
        SET nombreProfesion = ?
        WHERE codigoProfesion = ?
    """, (
        profesion.nombreProfesion,
        profesion.codigoProfesion,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoProfesion: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM profesiones WHERE codigoProfesion = ?", (codigoProfesion,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesiones")
    resultado = cursor.fetchall()

    listaProfesiones = []
    for datos in resultado:
        cargo = Profesion(
            codigoProfesion=datos[0],
            nombreProfesion=datos[1])
        listaProfesiones.append(cargo)

    return listaProfesiones