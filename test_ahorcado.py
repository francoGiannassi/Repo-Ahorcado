import unittest
from ahorcado import Ahorcado

class TestsLogIn(unittest.TestCase):
    
    def test_valida_usuario_anonimo(self):
        ahorcado = Ahorcado()
        ahorcado.setNombreUsuario("")
        self.assertEqual("",ahorcado.getNombreUsuario())

class TestsConfiguracion(unittest.TestCase):
    
    def test_valida_ninguna_palabra_cargada(self):
        ahorcado = Ahorcado()
        self.assertIn("", ahorcado.getPalabra())

    def test_valida_una_palabra_cargada(self):
        ahorcado = Ahorcado()
        self.assertIn("Ahorcado", ahorcado.getPalabra())

class TestsJuego(unittest.TestCase):

    def test_valida_letra_correcta(self):
        ahorcado = Ahorcado()
        self.assertRegex(ahorcado.getPalabra(),"a")
