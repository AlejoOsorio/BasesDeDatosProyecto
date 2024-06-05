import Database
from model.Empleado import Empleado


def findById(codigoEmpleado: str):
    empleado = None

    query = "SELECT * FROM empleados WHERE codigoEmpleado = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (codigoEmpleado,))
    resultado = cursor.fetchone()

    if resultado:

        empleado = Empleado(
            codigoEmpleado=resultado[0],
            cedulaEmpleado=resultado[1],
            nombreEmpleado=resultado[2],
            apellidoEmpleado=resultado[3],
            direccionResidenciaEmpleado=resultado[4],
            telefonoEmpleado=resultado[5],
            correoEmpleado=resultado[6],
            profesiones=[]
        )

        # Esta query busca las profesiones del empleado
        query = ("SELECT profesion "
                 "FROM detalleempleadosprofesiones "
                 "WHERE empleado = %s"
                 )

        cursor.execute(query, (codigoEmpleado,))
        resultado = cursor.fetchall()

        listaProfesiones = []
        for codigoProfesion in resultado:
            listaProfesiones.append(codigoProfesion[0])

        empleado.profesiones = listaProfesiones

    Database.cerrarConexion(conexion)
    return empleado


def findByCorreo(correoEmpleado: str):
    empleado = None

    query = "SELECT * FROM empleados WHERE correoEmpleado = %s"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (correoEmpleado,))
    resultado = cursor.fetchone()

    if resultado:

        empleado = Empleado(
            codigoEmpleado=resultado[0],
            cedulaEmpleado=resultado[1],
            nombreEmpleado=resultado[2],
            apellidoEmpleado=resultado[3],
            direccionResidenciaEmpleado=resultado[4],
            telefonoEmpleado=resultado[5],
            correoEmpleado=resultado[6],
            profesiones=[]
        )

        # Esta query busca las profesiones del empleado
        query = ("SELECT profesion "
                 "FROM detalleempleadosprofesiones "
                 "WHERE empleado = %s"
                 )

        cursor.execute(query, (empleado.codigoEmpleado,))
        resultado = cursor.fetchall()

        listaProfesiones = []
        for codigoProfesion in resultado:
            listaProfesiones.append(codigoProfesion[0])

        empleado.profesiones = listaProfesiones

    Database.cerrarConexion(conexion)
    return empleado


def save(empleado: Empleado):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO empleados (codigoEmpleado, cedulaEmpleado, nombreEmpleado, apellidoEmpleado, direccionResidenciaEmpleado, telefonoEmpleado, correoEmpleado) VALUES (?,?,?,?,?,?,?)",
        (empleado.codigoEmpleado, empleado.cedulaEmpleado, empleado.nombreEmpleado, empleado.apellidoEmpleado,
         empleado.direccionResidenciaEmpleado, empleado.telefonoEmpleado,
         empleado.correoEmpleado))
    conexion.commit()
    Database.cerrarConexion(conexion)

def saveDetalleEmpleado(codigoEmpleado: str, codigoPofesion: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        u"INSERT INTO detalleempleadosprofesiones (empleado, profesion) VALUES (?,?)",
        (codigoEmpleado, codigoPofesion))
    conexion.commit()
    Database.cerrarConexion(conexion)


def update(empleado: Empleado):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE empleados 
        SET cedulaEmpleado = ?, 
            nombreEmpleado = ?, 
            apellidoEmpleado = ?, 
            direccionResidenciaEmpleado = ?, 
            telefonoEmpleado = ?, 
            correoEmpleado = ? 
        WHERE codigoEmpleado = ?
    """, (
        empleado.cedulaEmpleado,
        empleado.nombreEmpleado,
        empleado.apellidoEmpleado,
        empleado.direccionResidenciaEmpleado,
        empleado.telefonoEmpleado,
        empleado.correoEmpleado,
        empleado.codigoEmpleado
    ))
    conexion.commit()
    Database.cerrarConexion(conexion)


def delete(codigoEmpleado: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM empleados WHERE codigoEmpleado = ?", (codigoEmpleado,))
    conexion.commit()
    Database.cerrarConexion(conexion)

def deleteProfesionesEmpleado(codigoEmpleado: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(u"DELETE FROM detalleempleadosprofesiones WHERE empleado = ?", (codigoEmpleado,))
    conexion.commit()
    Database.cerrarConexion(conexion)


def findAll():
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT e.codigoEmpleado, e.cedulaEmpleado, e.nombreEmpleado, e.apellidoEmpleado, e.direccionResidenciaEmpleado, e.telefonoEmpleado, e.correoEmpleado, pro.codigoProfesion "
        "FROM empleados e "
        "JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado "
        "JOIN profesiones pro ON dep.profesion = pro.codigoProfesion "
        )
    resultado = cursor.fetchall()

    empleados_dict = {}

    for datos in resultado:
        codigoEmpleado = datos[0]  # El índice correcto para codigoEmpleado es 0
        if codigoEmpleado not in empleados_dict:
            empleado = Empleado(
                codigoEmpleado=datos[0],  # Utiliza datos[0] para codigoEmpleado
                cedulaEmpleado=datos[1],
                nombreEmpleado=datos[2],
                apellidoEmpleado=datos[3],
                direccionResidenciaEmpleado=datos[4],
                telefonoEmpleado=datos[5],
                correoEmpleado=datos[6],
                profesiones=[]
            )
            empleados_dict[codigoEmpleado] = empleado

        empleados_dict[codigoEmpleado].profesiones.append(datos[7])

    lista_clientes = list(empleados_dict.values())
    return lista_clientes


def findAllByCargo(nombrecargo: str):
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT e.codigoEmpleado, e.cedulaEmpleado, e.nombreEmpleado, e.apellidoEmpleado, e.direccionResidenciaEmpleado, e.telefonoEmpleado, e.correoEmpleado, pro.codigoProfesion "
        "FROM empleados e "
        "JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado "
        "JOIN profesiones pro ON dep.profesion = pro.codigoProfesion "
        "JOIN contratos c ON e.codigoEmpleado = c.empleado "
        "JOIN cargos ca ON c.cargo = ca.codigoCargo "
        "WHERE ca.nombreCargo = ?", (nombrecargo,)
        )
    resultado = cursor.fetchall()

    empleados_dict = {}

    for datos in resultado:
        codigoEmpleado = datos[0]  # El índice correcto para codigoEmpleado es 0
        if codigoEmpleado not in empleados_dict:
            empleado = Empleado(
                codigoEmpleado=datos[0],  # Utiliza datos[0] para codigoEmpleado
                cedulaEmpleado=datos[1],
                nombreEmpleado=datos[2],
                apellidoEmpleado=datos[3],
                direccionResidenciaEmpleado=datos[4],
                telefonoEmpleado=datos[5],
                correoEmpleado=datos[6],
                profesiones=[]
            )
            empleados_dict[codigoEmpleado] = empleado

        empleados_dict[codigoEmpleado].profesiones.append(datos[7])

    lista_clientes = list(empleados_dict.values())
    return lista_clientes
