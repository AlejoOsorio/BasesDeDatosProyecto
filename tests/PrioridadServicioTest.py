import unittest

import services.PrioridadServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearPrioridad(self):
        services.PrioridadServicioImpl.crearPrioridad("PrioridadPrueba","PrioridadPrueba")
        self.assertEqual("PrioridadPrueba",services.PrioridadServicioImpl.obtenerPrioridad("PrioridadPrueba").nombrePrioridad)

    def test_actualizarPrioridad(self):
        services.PrioridadServicioImpl.actualizarPrioridad("PrioridadPrueba","PrioridadPrueba")
        self.assertEqual("PrioridadPrueba",services.PrioridadServicioImpl.obtenerPrioridad("PrioridadPrueba").nombrePrioridad)

    def test_eliminarPrioridad(self):
        services.PrioridadServicioImpl.eliminarPrioridad("PrioridadPrueba")

    def test_obtenerPrioridad(self):
        prioridad = services.PrioridadServicioImpl.obtenerPrioridad("PrioridadPrueba")
        self.assertEqual("PrioridadPrueba2",prioridad.nombrePrioridad)

    def test_obtenerListaCargos(self):
        lista = services.PrioridadServicioImpl.obtenerListaPrioridades()
        for prioridad in lista:
            print("Codigo: "+prioridad.codigoPrioridad+" nombre: "+prioridad.nombrePrioridad)

if __name__ == '__main__':
    unittest.main()
