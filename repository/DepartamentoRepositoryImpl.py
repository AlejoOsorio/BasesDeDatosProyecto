import Database
from model.Departamento import Departamento


def findById(codigoDepartamento: str):
    departamento = None

    query = "SELECT * FROM departamentos WHERE codigoDepartamento = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoDepartamento,))
    resultado = cursor.fetchone()

    if resultado:
        departamento = Departamento(
            codigoDepartamento=resultado[0],
            nombreDepartamento=resultado[1],
            poblacionDepartamento=resultado[2],
        )
    Database.cerrarConexion(conexion)
    return departamento

def save(departamento: Departamento):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO departamentos (codigoDepartamento, nombreDepartamento, poblacion) VALUES (?,?,?)",
        (departamento.codigoDepartamento, departamento.nombreDepartamento, departamento.poblacionDepartamento))
    conexion.commit()
    Database.cerrarConexion(conexion)

def update(departamento: Departamento):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE departamentos 
        SET nombreDepartamento = ?, 
            poblacion = ?  
        WHERE codigoDepartamento = ?
    """, (
        departamento.nombreDepartamento,
        departamento.poblacionDepartamento,
        departamento.codigoDepartamento,
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)

def delete(codigoDepartamento: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM departamentos WHERE codigoDepartamento = ?", (codigoDepartamento,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM departamentos")
    resultado = cursor.fetchall()

    listaDepartamentos = []
    for datos in resultado:
        departamento = Departamento(
            codigoDepartamento=datos[0],
            nombreDepartamento=datos[1],
            poblacionDepartamento=datos[2])
        listaDepartamentos.append(departamento)

    return listaDepartamentos