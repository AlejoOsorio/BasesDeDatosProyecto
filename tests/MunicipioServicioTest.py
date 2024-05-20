import unittest

import services.MunicipioServicioImpl


class MyTestCase(unittest.TestCase):

    def test_crearMunicipio(self):
        services.MunicipioServicioImpl.crearMunicipio("m1","Armenia","p1","d1",12354)
        self.assertEqual("Armenia",services.MunicipioServicioImpl.obtenerMunicipio("m1").nombreMunicipio)

    def test_actualizarMunicipio(self):
        services.MunicipioServicioImpl.actualizarMunicipio("m1","Quimbaya","p4","d1",354)
        self.assertEqual("Quimbaya",services.MunicipioServicioImpl.obtenerMunicipio("m1").nombreMunicipio)

    def test_eliminarMunicipio(self):
        services.MunicipioServicioImpl.eliminarMunicipio("m1")

    def test_obtenerMunicipio(self):
        municipio = services.MunicipioServicioImpl.obtenerMunicipio("m1")
        self.assertEqual("Quimbaya",municipio.nombreMunicipio)

    def test_obtenerListaMunicipios(self):
        lista = services.MunicipioServicioImpl.obtenerListaMunicipios()
        for municipio in lista:
            print("Codigo: "+municipio.codigoMunicipio+" nombre: "+municipio.nombreMunicipio+" prioridad: "+municipio.prioridad+" departamento: "+municipio.departamento+" poblacion: "+str(municipio.poblacionMunicipio))

if __name__ == '__main__':
    unittest.main()
