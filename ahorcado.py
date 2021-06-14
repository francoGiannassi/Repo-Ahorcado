class Ahorcado:

    nombreUsuario = None
    palabra = "Ahorcado"
    letrasCorrectas = []
    letrasIncorrectas = []
    intentosFallidos = 0

    def getNombreUsuario(self):
        return self.nombreUsuario

    def setNombreUsuario(self,nombre):
        self.nombreUsuario = nombre

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
