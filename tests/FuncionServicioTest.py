import unittest

import services.FuncionServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearFuncion(self):
        services.FuncionServicioImpl.crearFuncion("FuncionPrueba","FuncionPrueba","FuncionPrueba","c1")
        self.assertEqual("FuncionPrueba",services.FuncionServicioImpl.obtenerFuncion("FuncionPrueba").nombreFuncion)

    def test_actualizarFuncion(self):
        services.FuncionServicioImpl.actualizarFuncion("FuncionPrueba","FuncionPrueba2","FuncionPrueba2","c2")
        self.assertEqual("FuncionPrueba2",services.FuncionServicioImpl.obtenerFuncion("FuncionPrueba").nombreFuncion)

    def test_eliminarFuncion(self):
        services.FuncionServicioImpl.eliminarFuncion("FuncionPrueba")

    def test_obtenerFuncion(self):
        funcion = services.FuncionServicioImpl.obtenerFuncion("FuncionPrueba")
        self.assertEqual("FuncionPrueba",funcion.nombreFuncion)

    def test_obtenerListaFunciones(self):
        lista = services.FuncionServicioImpl.obtenerListaFunciones()
        for funcion in lista:
            print("Codigo: "+funcion.codigoFuncion+" nombre: "+funcion.nombreFuncion+" descripcion: "+funcion.descripcionFuncion+" cargo: "+funcion.cargoFuncion)

if __name__ == '__main__':
    unittest.main()
