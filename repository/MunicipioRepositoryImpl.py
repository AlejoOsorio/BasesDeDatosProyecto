import Database
from model.Municipio import Municipio


def findById(codigoMunicipio: str):
    municipio = None

    query = "SELECT * FROM municipios WHERE codigoMunicipio = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoMunicipio,))
    resultado = cursor.fetchone()

    if resultado:
        municipio = Municipio(
            codigoMunicipio=resultado[0],
            nombreMunicipio=resultado[1],
            prioridad=resultado[2],
            departamento=resultado[3],
            poblacionMunicipio=resultado[4]
        )
    Database.cerrarConexion(conexion)
    return municipio

def save(municipo: Municipio):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO municipios (codigoMunicipio, nombreMunicipio, prioridad, departamento, poblacion) VALUES (?,?,?,?,?)",
        (municipo.codigoMunicipio, municipo.nombreMunicipio, municipo.prioridad, municipo.departamento, municipo.poblacionMunicipio))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(municipio: Municipio):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE municipios 
        SET nombreMunicipio = ?, 
            prioridad = ?,
            departamento = ?,
            poblacion = ?  
        WHERE codigoMunicipio = ?
    """, (
        municipio.nombreMunicipio,
        municipio.prioridad,
        municipio.departamento,
        municipio.poblacionMunicipio,
        municipio.codigoMunicipio,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoMunicipio: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM municipios WHERE codigoMunicipio = ?", (codigoMunicipio,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM municipios")
    resultado = cursor.fetchall()

    listaMunicipios = []
    for datos in resultado:
        municipio = Municipio(
            codigoMunicipio=datos[0],
            nombreMunicipio=datos[1],
            prioridad=datos[2],
            departamento=datos[3],
            poblacionMunicipio=datos[4]
        )
        listaMunicipios.append(municipio)

    return listaMunicipios