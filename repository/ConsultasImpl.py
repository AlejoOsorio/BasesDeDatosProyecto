import Database


def consulta_empleados_nivel_principal(campos, nombreMunicipio="", nombreSucursal="", fechaInicio="", fechaFin="",
                                       nombreCargo=""):
    query = (
        f"SElECT {campos} "
        "FROM empleados e "
        "JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado "
        "JOIN profesiones p ON dep.profesion = p.codigoProfesion "
        "JOIN contratos con ON e.codigoEmpleado = con.empleado "
        "JOIN cargos car ON con.cargo = car.codigoCargo "
        "JOIN sucursales s ON con.sucursal = s.codigoSucursal "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d ON m.departamento = d.codigoDepartamento "
        "WHERE m.nombreMunicipio LIKE ? AND "
        "s.nombreSucursal LIKE ? AND "
        "con.fechaContrato BETWEEN ? AND ? AND "
        "car.nombreCargo LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (
        "%" + nombreMunicipio + "%", "%" + nombreSucursal + "%", fechaInicio, fechaFin, "%" + nombreCargo + "%"))
    return cursor.fetchall()


def consulta_empleados_nivel_parametrico(campos, nombreMunicipio="", nombreSucursal="", nombreFuncion="",
                                         nombreProfesion=""):
    query = (
        f"SElECT {campos} "
        "FROM empleados e "
        "JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado "
        "JOIN profesiones p ON dep.profesion = p.codigoProfesion "
        "JOIN contratos con ON e.codigoEmpleado = con.empleado "
        "JOIN cargos car ON con.cargo = car.codigoCargo "
        "JOIN funciones f ON car.codigoCargo = f.cargo "
        "JOIN sucursales s ON con.sucursal = s.codigoSucursal "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d ON m.departamento = d.codigoDepartamento "
        "WHERE m.nombreMunicipio LIKE ? AND "
        "s.nombreSucursal LIKE ? AND "
        "f.nombreFuncion LIKE ? AND "
        "p.nombreProfesion LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (
        "%" + nombreMunicipio + "%", "%" + nombreSucursal + "%", "%" + nombreFuncion + "%",
        "%" + nombreProfesion + "%"))
    return cursor.fetchall()


def consulta_empleados_nivel_esporadico(campos, nombreSucursal="", nombreEmpleado=""):
    query = (
        f"SElECT {campos} "
        "FROM empleados e "
        "JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado "
        "JOIN profesiones p ON dep.profesion = p.codigoProfesion "
        "JOIN contratos con ON e.codigoEmpleado = con.empleado "
        "JOIN cargos car ON con.cargo = car.codigoCargo "
        "JOIN funciones f ON car.codigoCargo = f.cargo "
        "JOIN sucursales s ON con.sucursal = s.codigoSucursal "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d ON m.departamento = d.codigoDepartamento "
        "WHERE s.nombreSucursal LIKE ? AND "
        "e.nombreEmpleado LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, ("%" + nombreSucursal + "%", "%" + nombreEmpleado + "%"))
    return cursor.fetchall()


def consulta_sucursales_nivel_principal(campos, poblacion="", nombrePrioridad="", nombreMunicipio="",
                                        nombreDepartamento="", nombreSucursal=""):
    if not poblacion:
        poblacion = None
    query = (
        f"SElECT {campos} "
        "FROM sucursales s "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d on d.codigoDepartamento = m.departamento "
        "JOIN prioridades p on p.codigoPrioridad = m.prioridad "
        "WHERE (? IS NULL OR m.poblacion = ?) AND "
        "p.nombrePrioridad LIKE ? AND "
        "m.nombreMunicipio LIKE ? AND "
        "d.nombreDepartamento LIKE ? AND "
        "s.nombreSucursal LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query,
                   (poblacion, poblacion, "%" + nombrePrioridad + "%", "%" + nombreMunicipio + "%", "%" + nombreDepartamento + "%",
                    "%" + nombreSucursal + "%"))
    return cursor.fetchall()


def consulta_sucursales_nivel_parametrico(campos, poblacion="", nombreSucursal=""):
    if not poblacion:
        poblacion = None
    query = (
        f"SElECT {campos} "
        "FROM sucursales s "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d on d.codigoDepartamento = m.departamento "
        "JOIN prioridades p on p.codigoPrioridad = m.prioridad "
        "WHERE (? IS NULL OR d.poblacion = ?) AND "
        "s.nombreSucursal LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, (poblacion, poblacion, "%" + nombreSucursal + "%"))
    return cursor.fetchall()


def consulta_sucursales_nivel_esporadico(campos, nombreMunicipio="", nombreDepartamento=""):
    query = (
        f"SElECT {campos} "
        "FROM sucursales s "
        "JOIN municipios m ON s.municipio = m.codigoMunicipio "
        "JOIN departamentos d on d.codigoDepartamento = m.departamento "
        "JOIN prioridades p on p.codigoPrioridad = m.prioridad "
        "WHERE m.nombreMunicipio LIKE ? AND "
        "d.nombreDepartamento LIKE ?"
    )
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query, ("%" + nombreMunicipio + "%", "%" + nombreDepartamento + "%"))
    return cursor.fetchall()
