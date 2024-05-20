import unittest

import services.CargoServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearCargo(self):
        services.CargoServicioImpl.crearCargo("CargoPrueba","CargoNombreTest","1231256")
        self.assertEqual("CargoPrueba",services.CargoServicioImpl.obtenerCargo("CargoCodigoTest").nombreCargo)

    def test_actualizarCargo(self):
        services.CargoServicioImpl.actualizarCargo("CargoPrueba","CargoPruebaTest2",98765123)
        self.assertEqual("CargoPruebaTest2",services.CargoServicioImpl.obtenerCargo("CargoPrueba").nombreCargo)

    def test_eliminarCargo(self):
        services.CargoServicioImpl.eliminarCargo("CargoPrueba")

    def test_obtenerCargo(self):
        cargo = services.CargoServicioImpl.obtenerCargo("C1")
        self.assertEqual("cajero",cargo.nombreCargo)

    def test_obtenerListaCargos(self):
        lista = services.CargoServicioImpl.obtenerListaCargos()
        for cargos in lista:
            print("Codigo: "+cargos.codigoCargo+" nombre: "+cargos.nombreCargo+" salario: "+str(cargos.salarioCargo))

if __name__ == '__main__':
    unittest.main()
