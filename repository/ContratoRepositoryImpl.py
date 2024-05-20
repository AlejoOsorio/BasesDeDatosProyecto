import Database
from model.Contrato import Contrato


def findById(codigoContrato: str):
    contrato = None

    query = "SELECT * FROM contratos WHERE codigoContrato = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoContrato,))
    resultado = cursor.fetchone()

    if resultado:
        contrato = Contrato(
            codigoContrato=resultado[0],
            fechaInicioContrato=resultado[1],
            fechaTerminacionContrato=resultado[2],
            empleado=resultado[3],
            sucursal=resultado[4],
            cargo=resultado[5]
        )
    Database.cerrarConexion(conexion)
    return contrato

def save(contrato: Contrato):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO contratos (codigoContrato, fechaInicioContrato, fechaTerminacionContrato, empleado, sucursal, cargo) VALUES (?,?,?,?,?,?)",
        (contrato.codigoContrato, contrato.fechaInicioContrato, contrato.fechaTerminacionContrato, contrato.empleado, contrato.sucursal, contrato.cargo))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(contrato: Contrato):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE contratos 
        SET fechaInicioContrato = ?, 
            fechaTerminacionContrato = ?  ,
            empleado = ?,
            sucursal = ?,
            cargo = ?
        WHERE codigoContrato = ?
    """, (
        contrato.fechaInicioContrato,
        contrato.fechaTerminacionContrato,
        contrato.empleado,
        contrato.sucursal,
        contrato.cargo,
        contrato.codigoContrato
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoContrato: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM contratos WHERE codigoContrato = ?", (codigoContrato,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contratos")
    resultado = cursor.fetchall()

    listaContratos = []
    for datos in resultado:
        contrato = Contrato(
            codigoContrato=datos[0],
            fechaInicioContrato=datos[1],
            fechaTerminacionContrato=datos[2],
            empleado=datos[3],
            sucursal=datos[4],
            cargo=datos[5])
        listaContratos.append(contrato)

    return listaContratos