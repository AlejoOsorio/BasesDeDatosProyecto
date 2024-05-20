import unittest

import services.DepartamentoServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearDepartamento(self):
        services.DepartamentoServicioImpl.crearDepartamento("D1","Quindío","1234")
        self.assertEqual("Quindío",services.DepartamentoServicioImpl.obtenerDepartamento("D1").nombreDepartamento)

    def test_actualizarDepartamento(self):
        services.DepartamentoServicioImpl.actualizarDepartamento("D1","Risaralda",4321)
        self.assertEqual("Risaralda",services.DepartamentoServicioImpl.obtenerDepartamento("D1").nombreDepartamento)

    def test_eliminarDepartamento(self):
        services.DepartamentoServicioImpl.eliminarDepartamento("D1")

    def test_obtenerDepartamento(self):
        cargo = services.DepartamentoServicioImpl.obtenerDepartamento("D1")
        self.assertEqual("Quindío",cargo.nombreDepartamento)

    def test_obtenerListaDepartamentos(self):
        lista = services.DepartamentoServicioImpl.obtenerListaCargos()
        for departamento in lista:
            print("Codigo: "+departamento.codigoDepartamento+" nombre: "+departamento.nombreDepartamento+" poblacion: "+str(departamento.poblacionDepartamento))

if __name__ == '__main__':
    unittest.main()
