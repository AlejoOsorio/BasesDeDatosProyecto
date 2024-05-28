import Database

def consultaEmpleadoContratoInformacionSucursalCargo():
    query = "SELECT e.nombreEmpleado, e.apellidoEmpleado, c.fechaInicioContrato, c.fechaTerminacionContrato, s.nombreSucursal, car.nombreCargo FROM empleados e JOIN contratos c ON e.codigoEmpleado = c.empleado JOIN sucursales s ON c.sucursal = s.codigoSucursal JOIN cargos car ON c.cargo = car.codigoCargo"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def consultaEmpleadoProfesionesSucursales():
    query = "SELECT e.nombreEmpleado, e.apellidoEmpleado, p.nombreProfesion, s.nombreSucursal FROM empleados e JOIN detalleempleadosprofesiones dep ON e.codigoEmpleado = dep.empleado JOIN profesiones p ON dep.profesion = p.codigoProfesion JOIN contratos c ON e.codigoEmpleado = c.empleado JOIN sucursales s ON c.sucursal = s.codigoSucursal"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def consultaSucursalesMunicipiosAtencion():
    query = "SELECT s.nombreSucursal, s.direccionSucursal, m.nombreMunicipio, p.nombrePrioridad FROM sucursales s JOIN municipios m ON s.municipio = m.codigoMunicipio JOIN prioridades p ON m.prioridad = p.codigoPrioridad"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def consultaCargosFuncionesAsociadas():
    query = "SELECT c.nombreCargo, f.nombreFuncion, f.descripcionFuncion FROM cargos c JOIN funciones f ON c.codigoCargo = f.cargo"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def consultaEmpleados():
    query = "SELECT nombreEmpleado, apellidoEmpleado, correoEmpleado FROM empleados"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def consultaSucursalesPresupuestos():
    query = "SELECT nombreSucursal, presupuestoAnualSucursal FROM sucursales"
    conexion = Database.abrirConexion()
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()