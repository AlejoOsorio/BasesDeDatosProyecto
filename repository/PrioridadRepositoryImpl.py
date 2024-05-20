import Database
from model.Prioridad import Prioridad


def findById(codigoPrioridad: str):
    prioridad = None

    query = "SELECT * FROM prioridades WHERE codigoPrioridad = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoPrioridad,))
    resultado = cursor.fetchone()

    if resultado:
        prioridad = Prioridad(
            codigoPrioridad=resultado[0],
            nombrePrioridad=resultado[1]
        )
    Database.cerrarConexion(conexion)
    return prioridad

def save(prioridad: Prioridad):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO prioridades (codigoPrioridad, nombrePrioridad) VALUES (?,?)",
        (prioridad.codigoPrioridad, prioridad.nombrePrioridad))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(prioridad: Prioridad):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE prioridades 
        SET nombrePrioridad = ?         
        WHERE codigoPrioridad = ?
    """, (
        prioridad.nombrePrioridad,
        prioridad.codigoPrioridad,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoPrioridad: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM prioridades WHERE codigoPrioridad = ?", (codigoPrioridad,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM prioridades")
    resultado = cursor.fetchall()

    listaPrioridades = []
    for datos in resultado:
        proridad = Prioridad(
            codigoPrioridad=datos[0],
            nombrePrioridad=datos[1])
        listaPrioridades.append(proridad)

    return listaPrioridades