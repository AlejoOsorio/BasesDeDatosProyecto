import datetime
import unittest

import services.BitacoraServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearBitacora(self):
        services.BitacoraServicioImpl.crearBitacora("B1",datetime.date.today(),datetime.datetime.now(),datetime.datetime.now(),"u1",datetime.date.today())
        self.assertEqual("B2",services.BitacoraServicioImpl.obtenerBitacora("B1").codigoBitacora)

    def test_obtenerBitacora(self):
        cargo = services.BitacoraServicioImpl.obtenerBitacora("B1")
        self.assertEqual("B1",cargo.codigoBitacora)

    def test_obtenerListaBitacoras(self):
        lista = services.BitacoraServicioImpl.obtenerListaBitacoras()
        for bitacoras in lista:
            print("Codigo: "+bitacoras.codigoBitacora+" numero ingreso: "+str(bitacoras.numeroIngreso)+" fecha ingreso: "+ str(bitacoras.fechaIngreso)+" hora ingreso: "+ str(bitacoras.horaIngreso)+" hora salida: "+str(bitacoras.horaSalida)+" usuario: "+bitacoras.usuario+" fecha salida: "+str(bitacoras.fechaSalida))

if __name__ == '__main__':
    unittest.main()
