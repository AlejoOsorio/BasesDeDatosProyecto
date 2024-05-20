import unittest

import services.ProfesionServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearProfesion(self):
        services.ProfesionServicioImpl.crearProfesion("ProfesionPrueba","ProfesionPrueba")
        self.assertEqual("ProfesionPrueba",services.ProfesionServicioImpl.obtenerProfesion("ProfesionPrueba").nombreProfesion)

    def test_actualizarProfesion(self):
        services.ProfesionServicioImpl.actualizarProfesion("ProfesionPrueba","ProfesionPrueba2")
        self.assertEqual("ProfesionPrueba2",services.ProfesionServicioImpl.obtenerProfesion("ProfesionPrueba").nombreProfesion)

    def test_eliminarProfesion(self):
        services.ProfesionServicioImpl.eliminarProfesion("ProfesionPrueba")

    def test_obtenerProfesion(self):
        profesion = services.ProfesionServicioImpl.obtenerProfesion("ProfesionPrueba")
        self.assertEqual("ProfesionPrueba",profesion.nombreProfesion)

    def test_obtenerListaProfesion(self):
        lista = services.ProfesionServicioImpl.obtenerListaProfesiones()
        for profesiones in lista:
            print("Codigo: "+profesiones.codigoProfesion+" nombre: "+profesiones.nombreProfesion)

if __name__ == '__main__':
    unittest.main()
