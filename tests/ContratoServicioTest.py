import datetime
import unittest

import services.ContratoServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearContrato(self):
        services.ContratoServicioImpl.crearContrato("C1","2024-06-21","2024-12-01","Cliente1","S1","c1")
        self.assertEqual(datetime.date(2024,6,21),services.ContratoServicioImpl.obtenerContrato("C1").fechaInicioContrato)

    def test_actualizarContrato(self):
        services.ContratoServicioImpl.actualizarContrato("C1","2024-10-29","2024-12-01","Cliente1","S1","c1")
        self.assertEqual("C1",services.ContratoServicioImpl.obtenerContrato("C1").codigoContrato)

    def test_eliminarContrato(self):
        services.ContratoServicioImpl.eliminarContrato("C1")

    def test_obtenerContrato(self):
        contrato = services.ContratoServicioImpl.obtenerContrato("C1")
        self.assertEqual("C1",contrato.codigoContrato)

    def test_obtenerListaContratos(self):
        lista = services.ContratoServicioImpl.obtenerListaContratos()
        for contratos in lista:
            print("Codigo: "+contratos.codigoContrato+" fecha inicio: "+str(contratos.fechaInicioContrato)+" fecha terminacion: "+str(contratos.fechaTerminacionContrato)+" sucursal: "+contratos.sucursal+" empleado: "+contratos.empleado+" cargo: "+contratos.cargo)

if __name__ == '__main__':
    unittest.main()
