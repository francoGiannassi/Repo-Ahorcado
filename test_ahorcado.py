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

class TestsIngresoLetra(unittest.TestCase):

    def test_valida_letra_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("a")
        self.assertIn("a",ahorcado.getLetrasCorrectas())
    
    def test_valida_letra_incorrecta(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("e")
        self.assertIn("e",ahorcado.getLetrasIncorrectas())

    def test_valida_letra_mayuscula(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("H")
        self.assertIn("H",ahorcado.getLetrasCorrectas())

    def test_valida_caracter_no_alfabetico(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("$")
        self.assertIn("$",ahorcado.getLetrasIncorrectas())
    
    def test_valida_caracter_vacio(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("")
        self.assertIn("",ahorcado.getLetrasIncorrectas())

    def test_es_letra_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("c")
        self.assertTrue(ahorcado.esLetraCorrecta("c"))
    
    def test_es_letra_incorrecta(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("t")
        self.assertFalse(ahorcado.esLetraCorrecta("t"))
    
    def test_palabra_parcial_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("A")
        ahorcado.ingresaLetra("H")
        ahorcado.ingresaLetra("C")
        ahorcado.ingresaLetra("D")
        self.assertEqual(ahorcado.getPalabraParcial(),"AH--CAD-")
    
    def test_valida_conteo_intentos_fallidos(self):
        ahorcado = Ahorcado()
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("i")
        ahorcado.ingresaLetra("m")
        self.assertEqual(ahorcado.getIntentosFallidos(),3)

    def test_valida_tope_maximo_intentos_fallidos(self):
        ahorcado1 = Ahorcado()
        ahorcado1.ingresaLetra("f")
        ahorcado1.ingresaLetra("i")
        ahorcado1.ingresaLetra("m")
        ahorcado1.ingresaLetra("u")
        ahorcado1.ingresaLetra("j")
        ahorcado1.ingresaLetra("k")
        ahorcado1.ingresaLetra("p")
        self.assertEqual(ahorcado1.getIntentosFallidos(),7)

class TestsResultadoFinal(unittest.TestCase):

    def test_valida_partida_perdida(self):
        ahorcado2 = Ahorcado()
        ahorcado2.ingresaLetra("f")
        ahorcado2.ingresaLetra("i")
        ahorcado2.ingresaLetra("m")
        ahorcado2.ingresaLetra("u")
        ahorcado2.ingresaLetra("j")
        ahorcado2.ingresaLetra("k")
        ahorcado2.ingresaLetra("p")
        self.assertEqual("Perdido",ahorcado2.getEstadoFinalJuego())

    def test_valida_partida_ganada(self):
        ahorcado3 = Ahorcado()
        ahorcado3.ingresaLetra("a")
        ahorcado3.ingresaLetra("h")
        ahorcado3.ingresaLetra("o")
        ahorcado3.ingresaLetra("r")
        ahorcado3.ingresaLetra("c")
        ahorcado3.ingresaLetra("d")
        self.assertEqual("Ganado",ahorcado3.getEstadoFinalJuego())


