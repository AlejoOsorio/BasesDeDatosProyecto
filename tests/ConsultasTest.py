import unittest

import repository.ConsultasImpl


class MyTestCase(unittest.TestCase):

    def test_consultaEmpleadoContratoInformacionSucursalCargo(self):
        print(repository.ConsultasImpl.consultaEmpleadoContratoInformacionSucursalCargo())

    def test_consultaEmpleadoProfesionesSucursales(self):
        print(repository.ConsultasImpl.consultaEmpleadoProfesionesSucursales())

    def test_consultaSucursalesMunicipiosAtencion(self):
        print(repository.ConsultasImpl.consultaSucursalesMunicipiosAtencion())

    def test_consultaCargosFuncionesAsociadas(self):
        print(repository.ConsultasImpl.consultaCargosFuncionesAsociadas())

    def test_consultaEmpleados(self):
        print(repository.ConsultasImpl.consultaEmpleados())

    def test_consultaSucursalesPresupuestos(self):
        print(repository.ConsultasImpl.consultaSucursalesPresupuestos())



if __name__ == '__main__':
    unittest.main()
