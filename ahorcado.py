from usuario import Usuario
import random

class Ahorcado:

    usuario1 = Usuario()
    usuario1.setNombre("juan2")

    usuario2 = Usuario()
    usuario2.setNombre("pedro3")

    usuario3 = Usuario()
    usuario3.setNombre("silvia4") 

    usuario4 = Usuario()
    usuario4.setNombre("hernan5") 

    usuarioActual = Usuario()
    usuarioActual.setNombre("Franco1")

    usuarios = [usuario1,usuario2,usuario3,usuario4,usuarioActual]

    palabrasFaciles = ["Ola","Rio","Casa","Via","Sol"]
    palabrasIntermedias = ["Juego","Ahorcado","Visual","Estudio","Codigo"]
    palabrasDificiles = ["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"]
    palabra = ""

    letrasCorrectas = []
    letrasIncorrectas = []
    intentosFallidos = 0

    def getPalabrasFaciles(self):
        return self.palabrasFaciles

    def getPalabrasIntermedias(self):
        return self.palabrasIntermedias

    def getPalabrasDificiles(self):
        return self.palabrasDificiles

    def setPalabra(self,palabra):
        self.palabra = palabra

    def seleccionarPalabraRandom(self,palabra,palabras):
        palabra = random.choice(palabras)
        return palabra

    def getUsuarioActual(self):
        return self.usuarioActual
    
    def existeUsuario(self,nombre):
        if nombre in self.getNombresUsuarios():
            return True
        else:
            return False

    def getUsuarios(self):
        return self.usuarios

    def getNombresUsuarios(self):
        nombres = []
        for us in self.usuarios:
            nombres.append(us.getNombre())
        return nombres

    def getPalabra(self):
        return self.palabra

    def ingresaLetra(self, letra):
        if letra == "" or not letra.isalpha():
            self.letrasIncorrectas.append(letra)
        elif self.esLetraCorrecta(letra):
            self.letrasCorrectas.append(letra.lower())
            self.letrasCorrectas.append(letra.upper())
        else:
            self.letrasIncorrectas.append(letra.lower())
            self.letrasIncorrectas.append(letra.upper())
            self.sumarIntentoFallido()
        
    def getLetrasCorrectas(self):
        return self.letrasCorrectas

    def getLetrasIncorrectas(self):
        return self.letrasIncorrectas

    def esLetraCorrecta(self, letra):
        if letra.lower() in self.palabra:
            return True
        else:
            return False
        
    def getPalabraParcial(self):
        palabraParcial = ""
        for letra in self.palabra:
            if letra in self.letrasCorrectas:
                palabraParcial += letra.upper()
            else: 
                palabraParcial += "-"
        return palabraParcial
    
    def sumarIntentoFallido(self):
        self.intentosFallidos+=1
    
    def getIntentosFallidos(self):
        return self.intentosFallidos

    def getEstadoFinalJuego(self):
        if self.intentosFallidos == 7:
            return "Perdido"
        elif self.esPalabraFinal():
            return "Ganado"
    
    def esPalabraFinal(self):
        esPalabra = True
        for letra in self.palabra:
            if letra not in self.letrasCorrectas:
                esPalabra = False
        return esPalabra


