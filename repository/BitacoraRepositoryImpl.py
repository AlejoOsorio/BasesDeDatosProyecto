import Database
from model.Bitacora import Bitacora


def findById(codigoBitacora: str):
    bitacora = None

    query = "SELECT * FROM bitacoras WHERE codigoBitacora = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoBitacora,))
    resultado = cursor.fetchone()

    if resultado:
        bitacora = Bitacora(
            codigoBitacora=resultado[0],
            numeroIngreso=resultado[1],
            fechaIngreso=resultado[2],
            horaIngreso=resultado[3],
            horaSalida=resultado[4],
            usuario=resultado[5],
            fechaSalida=resultado[6]
        )
    Database.cerrarConexion(conexion)
    return bitacora

def findByNumeroIngreso(numeroIngreso: str):
    bitacora = None

    query = "SELECT * FROM bitacoras WHERE numeroIngreso = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (numeroIngreso,))
    resultado = cursor.fetchone()

    if resultado:
        bitacora = Bitacora(
            codigoBitacora=resultado[0],
            numeroIngreso=resultado[1],
            fechaIngreso=resultado[2],
            horaIngreso=resultado[3],
            horaSalida=resultado[5],
            usuario=resultado[6],
            fechaSalida=resultado[7]
        )
    Database.cerrarConexion(conexion)
    return bitacora

def save(bitacora: Bitacora):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()

    query = "SELECT COUNT(*) FROM bitacoras"
    cursor.execute(query)

    cantidad = cursor.fetchone()[0]+1

    cursor.execute(
        u"INSERT INTO bitacoras (codigoBitacora, numeroIngreso, fechaIngreso, horaIngreso, horaSalida, usuario, fechaSalida) VALUES (?,?,?,?,?,?,?)",
        (bitacora.codigoBitacora, cantidad, bitacora.fechaIngreso, bitacora.horaIngreso, bitacora.horaSalida, bitacora.usuario, bitacora.fechaSalida ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM bitacoras")
    resultado = cursor.fetchall()

    listaBitacoras = []
    for datos in resultado:
        bitacora = Bitacora(
            codigoBitacora=datos[0],
            numeroIngreso=datos[1],
            fechaIngreso=datos[2],
            horaIngreso=datos[3],
            horaSalida=datos[4],
            usuario=datos[5],
            fechaSalida=datos[6]
        )
        listaBitacoras.append(bitacora)

    return listaBitacoras