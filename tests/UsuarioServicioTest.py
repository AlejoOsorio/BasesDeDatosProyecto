import unittest

import services.UsuarioServicioImpl
from model.NivelUsuario import NivelUsuario


class MyTestCase(unittest.TestCase):

    def test_crearUsuario(self):
        services.UsuarioServicioImpl.crearUsuario("U1", "admin", "admin123", NivelUsuario.PRINCIPAL.value)
        self.assertEqual("admin", services.UsuarioServicioImpl.obtenerUsuario("U1").nombreUsuario)

    def test_actualizarUsuario(self):
        services.UsuarioServicioImpl.actualizarUsuario("U1", "administrador", "administrador123",
                                                       NivelUsuario.PRINCIPAL.value)
        self.assertEqual("administrador", services.UsuarioServicioImpl.obtenerUsuario("U1").nombreUsuario)

    def test_eliminarUsuario(self):
        services.UsuarioServicioImpl.eliminarUsuario("U1")

    def test_obtenerUsuario(self):
        usuario = services.UsuarioServicioImpl.obtenerUsuario("u1")
        self.assertEqual("administrador", usuario.nombreUsuario)

    def test_obtenerListaUsuarios(self):
        lista = services.UsuarioServicioImpl.obtenerListaUsuarios()
        for usuario in lista:
            print(
                "Codigo: " + usuario.codigoUsuario + " nombre: " + usuario.nombreUsuario + " clave: " + usuario.claveUsuario + " fecha creación: " + str(usuario.fechaCreacionUsuario) + " nivel: " + usuario.nivelUsuario)


if __name__ == '__main__':
    unittest.main()
