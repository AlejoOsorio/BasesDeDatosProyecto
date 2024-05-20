import unittest

import services.SucursalServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearSucursal(self):
        services.SucursalServicioImpl.crearSucursal("S1","Sucursal sede Armenia",1050000000,"Centro","m1")
        self.assertEqual("Sucursal sede Armenia",services.SucursalServicioImpl.obtenerSucursal("S1").nombreSucursal)

    def test_actualizarSucursal(self):
        services.SucursalServicioImpl.actualizarSucursal("S1","Sucursal sede Armenia",950000000,"Las delicias","m1")
        self.assertEqual("Las delicias",services.SucursalServicioImpl.obtenerSucursal("S1").direccionSucursal)

    def test_eliminarSucursal(self):
        services.SucursalServicioImpl.eliminarSucursal("S1")

    def test_obtenerSucursal(self):
        sucursal = services.SucursalServicioImpl.obtenerSucursal("S1")
        self.assertEqual("Sucursal sede Armenia",sucursal.nombreSucursal)

    def test_obtenerListaSucursales(self):
        lista = services.SucursalServicioImpl.obtenerListaSucursal()
        for sucursal in lista:
            print("Codigo: "+sucursal.codigoSucursal+" nombre: "+sucursal.nombreSucursal+" presupuesto: "+str(sucursal.presupuestoAnual)+" direccion: "+sucursal.direccionSucursal+" municipio: "+sucursal.municipio)

if __name__ == '__main__':
    unittest.main()
