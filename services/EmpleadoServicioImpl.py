import Database
import repository.EmpleadoRepositoryImpl
from model.Empleado import Empleado


def crearEmpleado(codigoEmpleado, cedulaEmpleado, nombreEmpleado, apellidoEmpleado, direccionResidenciaEmpleado, telefonoEmpleado, correoEmpleado):
    if repository.EmpleadoRepositoryImpl.findById(codigoEmpleado):
        raise RuntimeError("Ya existe un empleado con este codigo")
    if repository.EmpleadoRepositoryImpl.findByCorreo(correoEmpleado):
        raise RuntimeError("Ya existe un empleado con este correo")

    repository.EmpleadoRepositoryImpl.save(
        empleado=Empleado(
        codigoEmpleado=codigoEmpleado,
        cedulaEmpleado=cedulaEmpleado,
        nombreEmpleado=nombreEmpleado,
        apellidoEmpleado=apellidoEmpleado,
        direccionResidenciaEmpleado=direccionResidenciaEmpleado,
        telefonoEmpleado=telefonoEmpleado,
        correoEmpleado=correoEmpleado,
        profesiones=[]
    ))

def actualizarEmpleado(codigoEmpleado, cedulaEmpleado, nombreEmpleado, apellidoEmpleado, direccionResidenciaEmpleado, telefonoEmpleado, correoEmpleado):
    empleado = repository.EmpleadoRepositoryImpl.findById(codigoEmpleado)
    if empleado is None:
        raise RuntimeError("No existe un empleado con este codigo")

    empleadoBuscadoCorreo = repository.EmpleadoRepositoryImpl.findByCorreo(correoEmpleado)
    if  empleadoBuscadoCorreo is not None and empleadoBuscadoCorreo.codigoEmpleado != empleado.codigoEmpleado:
        raise RuntimeError("Ya existe un empleado con este correo")



    empleado.cedulaEmpleado=cedulaEmpleado
    empleado.nombreEmpleado=nombreEmpleado
    empleado.apellidoEmpleado=apellidoEmpleado
    empleado.direccionResidenciaEmpleado=direccionResidenciaEmpleado
    empleado.telefonoEmpleado=telefonoEmpleado
    empleado.correoEmpleado=correoEmpleado

    repository.EmpleadoRepositoryImpl.update(empleado)

def eliminarEmpleado(codigoEmpleado: str):
    empleado = repository.EmpleadoRepositoryImpl.findById(codigoEmpleado)
    if empleado is None:
        raise RuntimeError("No existe un empleado con este codigo")
    repository.EmpleadoRepositoryImpl.delete(codigoEmpleado)

def obtenerEmpleado(codigoEmpleado):
    empleado = repository.EmpleadoRepositoryImpl.findById(codigoEmpleado)
    if empleado is None:
        raise RuntimeError("No existe un empleado con este codigo")
    return empleado

def obtenerListaEmpleados():
    return repository.EmpleadoRepositoryImpl.findAll()
