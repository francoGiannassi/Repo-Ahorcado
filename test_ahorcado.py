import unittest
from ahorcado import Ahorcado
from usuario import Usuario

class TestsLogIn(unittest.TestCase):
    
    def test_valida_usuario_anonimo(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("")
        self.assertEqual("",ahorcado.getUsuarioActual().getNombre())
        
    def test_nombre_usuario_incorrecto(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("Franco@123")
        self.assertFalse(ahorcado.getUsuarioActual().esNombreUsuarioCorrecto("Franco@123"))
    
    def test_nombre_usuario_correcto(self):
        ahorcado = Ahorcado()
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertTrue(ahorcado.getUsuarioActual().esNombreUsuarioCorrecto("Franco"))
    
    def test_valida_existencia_del_nombre(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setNombre("Franco")
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertTrue(ahorcado.existeUsuario(us.getNombre()))

    def test_valida_no_existencia_del_nombre(self):
        ahorcado = Ahorcado()
        us = Usuario()
        us.setNombre("Franco1")
        ahorcado.getUsuarioActual().setNombre("Franco")
        self.assertFalse(ahorcado.existeUsuario(us.getNombre()))


class TestsConfiguracion(unittest.TestCase):
    
    def test_valida_ninguna_palabra_cargada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("")
        self.assertIn("", ahorcado.getPalabra())

    def test_valida_una_palabra_cargada(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        self.assertIn("Ahorcado", ahorcado.getPalabrasIntermedias())

    def test_valida_dificultad_facil(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasFaciles(["Ola","Rio","Casa","Via","Sol"])
        self.assertIn("Ola",ahorcado.getPalabrasFaciles())

    def test_valida_dificultad_intermedia(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        self.assertIn("Codigo",ahorcado.getPalabrasIntermedias())

    def test_valida_dificultad_dificil(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabrasDificiles(["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"])
        self.assertIn("Onomatopeya",ahorcado.getPalabrasDificiles())

class TestsIngresoLetra(unittest.TestCase):

    def test_valida_letra_correcta(self):
        ahorcado7 = Ahorcado()
        ahorcado7.setPalabra("Ahorcado")
        ahorcado7.ingresaLetra("a")
        self.assertIn("a",ahorcado7.getLetrasCorrectas())
    
    def test_valida_letra_incorrecta(self):
        ahorcado9 = Ahorcado()
        ahorcado9.setPalabra("Ahorcado")
        ahorcado9.ingresaLetra("e")
        self.assertIn("e",ahorcado9.getLetrasIncorrectas())

    def test_valida_letra_mayuscula(self):
        ahorcado8 = Ahorcado()
        ahorcado8.setPalabra("Ahorcado")
        ahorcado8.ingresaLetra("H")
        self.assertIn("H",ahorcado8.getLetrasCorrectas())

    def test_valida_caracter_no_alfabetico(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("$")
        self.assertIn("$",ahorcado.getLetrasIncorrectas())
    
    def test_valida_caracter_vacio(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("")
        self.assertIn("",ahorcado.getLetrasIncorrectas())

    def test_es_letra_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("c")
        self.assertTrue(ahorcado.esLetraCorrecta("c"))
    
    def test_es_letra_incorrecta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("t")
        self.assertFalse(ahorcado.esLetraCorrecta("t"))
    
    def test_palabra_parcial_correcta(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("A")
        ahorcado.ingresaLetra("H")
        ahorcado.ingresaLetra("C")
        ahorcado.ingresaLetra("D")
        self.assertEqual(ahorcado.getPalabraParcial(),"AH--CAD-")
    
    def test_valida_conteo_intentos_fallidos(self):
        ahorcado = Ahorcado()
        ahorcado.setPalabra("Ahorcado")
        ahorcado.ingresaLetra("f")
        ahorcado.ingresaLetra("i")
        ahorcado.ingresaLetra("m")
        self.assertEqual(ahorcado.getIntentosFallidos(),3)

    def test_valida_tope_maximo_intentos_fallidos(self):
        ahorcado1 = Ahorcado()
        ahorcado1.setPalabra("Ahorcado")
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
        ahorcado2.setPalabra("Ahorcado")
        ahorcado2.setPalabra("Ahorcado")
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
        ahorcado3.setPalabra("Ahorcado")
        ahorcado3.ingresaLetra("a")
        ahorcado3.ingresaLetra("h")
        ahorcado3.ingresaLetra("o")
        ahorcado3.ingresaLetra("r")
        ahorcado3.ingresaLetra("c")
        ahorcado3.ingresaLetra("d")
        self.assertEqual("Ganado",ahorcado3.getEstadoFinalJuego())


