import unittest

import services.EmpleadoServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearCliente(self):
        services.EmpleadoServicioImpl.crearEmpleado("Cliente2","912345123","Andres","Quiceno","Carrera 4","3101234567","andres@email.com")
        self.assertEqual("Andres",services.EmpleadoServicioImpl.obtenerEmpleado("Cliente2").nombreEmpleado)

    def test_actualizarEmpleado(self):
        services.EmpleadoServicioImpl.actualizarEmpleado("Cliente1","1234","Pepito","Perez","Carrear 7","3101234567","Pepito@email.com")
        self.assertEqual("Pepito",services.EmpleadoServicioImpl.obtenerEmpleado("Cliente1").nombreEmpleado)

    def test_eliminarEmpleado(self):
        services.EmpleadoServicioImpl.eliminarEmpleado("Cliente1")

    def test_obtenerCliente(self):
        empleado = services.EmpleadoServicioImpl.obtenerEmpleado("Cliente1")
        print("Codigo: "+empleado.codigoEmpleado+" nombre: "+empleado.nombreEmpleado)
        for profesion in empleado.profesiones:
            print("Codigo: "+profesion)

    def test_obtenerListaClientes(self):
        empleados = services.EmpleadoServicioImpl.obtenerListaEmpleados()
        for empleado in empleados:
            print("Nombre: "+empleado.nombreEmpleado)
            for profesion in empleado.profesiones:
                print("Codigo profesion: "+profesion)


if __name__ == '__main__':
    unittest.main()
