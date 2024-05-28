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
            fechaContrato=resultado[1],
            fechaInicioContrato=resultado[2],
            fechaTerminacionContrato=resultado[3],
            empleado=resultado[4],
            sucursal=resultado[5],
            cargo=resultado[6]
        )
    Database.cerrarConexion(conexion)
    return contrato


def save(contrato: Contrato):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO contratos (codigoContrato, fechaContrato, fechaInicioContrato, fechaTerminacionContrato, empleado, sucursal, cargo) VALUES (?,?,?,?,?,?,?)",
        (contrato.codigoContrato, contrato.fechaInicioContrato, contrato.fechaTerminacionContrato, contrato.empleado,
         contrato.sucursal, contrato.cargo))
    conexion.commit()
    Database.cerrarConexion(conexion)


def update(contrato: Contrato):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE contratos 
        SET fechaContrato = ?,
            fechaInicioContrato = ?, 
            fechaTerminacionContrato = ?  ,
            empleado = ?,
            sucursal = ?,
            cargo = ?
        WHERE codigoContrato = ?
    """, (
        contrato.fechaContrato,
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
            fechaContrato=datos[1],
            fechaInicioContrato=datos[2],
            fechaTerminacionContrato=datos[3],
            empleado=datos[4],
            sucursal=datos[5],
            cargo=datos[6])
        listaContratos.append(contrato)

    return listaContratos
