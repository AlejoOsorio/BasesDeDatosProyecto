import Database
from model.Sucursal import Sucursal


def findById(codigoSucursal: str):
    sucursal = None

    query = "SELECT * FROM sucursales WHERE codigoSucursal = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoSucursal,))
    resultado = cursor.fetchone()

    if resultado:
        sucursal = Sucursal(
            codigoSucursal=resultado[0],
            nombreSucursal=resultado[1],
            presupuestoAnual=resultado[2],
            direccionSucursal=resultado[3],
            municipio=resultado[4]
        )
    Database.cerrarConexion(conexion)
    return sucursal

def save(sucursal: Sucursal):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO sucursales (codigoSucursal, nombreSucursal, presupuestoAnualSucursal, direccionSucursal, municipio) VALUES (?,?,?,?,?)",
        (sucursal.codigoSucursal, sucursal.nombreSucursal, sucursal.presupuestoAnual, sucursal.direccionSucursal, sucursal.municipio))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(sucursal: Sucursal):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE sucursales 
        SET nombreSucursal = ?, 
            presupuestoAnualSucursal = ?,
            direccionSucursal = ?,
            municipio = ?  
        WHERE codigoSucursal = ?
    """, (
        sucursal.nombreSucursal,
        sucursal.presupuestoAnual,
        sucursal.direccionSucursal,
        sucursal.municipio,
        sucursal.codigoSucursal
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoSucursal: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM sucursales WHERE codigoSucursal = ?", (codigoSucursal,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sucursales")
    resultado = cursor.fetchall()

    listaSucursales = []
    for datos in resultado:
        sucursal = Sucursal(
            codigoSucursal=datos[0],
            nombreSucursal=datos[1],
            presupuestoAnual=datos[2],
            direccionSucursal=datos[3],
            municipio=datos[4]
        )
        listaSucursales.append(sucursal)

    return listaSucursales