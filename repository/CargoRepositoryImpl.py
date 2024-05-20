import Database
from model.Cargo import Cargo


def findById(codigoCargo: str):
    cargo = None

    query = "SELECT * FROM cargos WHERE codigoCargo = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoCargo,))
    resultado = cursor.fetchone()

    if resultado:
        cargo = Cargo(
            codigoCargo=resultado[0],
            nombreCargo=resultado[1],
            salarioCargo=resultado[2],
        )
    Database.cerrarConexion(conexion)
    return cargo

def save(cargo: Cargo):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO cargos (codigoCargo, nombreCargo, salarioCargo) VALUES (?,?,?)",
        (cargo.codigoCargo, cargo.nombreCargo, cargo.salarioCargo))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(cargo: Cargo):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE cargos 
        SET nombreCargo = ?, 
            salarioCargo = ?  
        WHERE codigoCargo = ?
    """, (
        cargo.nombreCargo,
        cargo.salarioCargo,
        cargo.codigoCargo,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoCargo: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM cargos WHERE codigoCargo = ?", (codigoCargo,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cargos")
    resultado = cursor.fetchall()

    listaCargos = []
    for datos in resultado:
        cargo = Cargo(
            codigoCargo=datos[0],
            nombreCargo=datos[1],
            salarioCargo=datos[2])
        listaCargos.append(cargo)

    return listaCargos