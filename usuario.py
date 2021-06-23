class Usuario:

    nombre = ""
    contraseña = ""
    puntuacionMaxima = 0


    def __init__(self, nombre="",contraseña="" ,puntuacionMaxima=0):
        self.nombre = nombre
        self.puntuacionMaxima = puntuacionMaxima

    def __repr__(self):
        return repr((self.nombre, self.puntuacionMaxima))

    def esNombreUsuarioCorrecto(self,nombre):
        if len(nombre) <= 8:
            return True
        else:
            return False

    def esContraseñaCorrecta(self,contraseña):
        if len(contraseña) <= 15:
            return True
        else:
            return False

    def setNombre(self,nombre):
        if self.esNombreUsuarioCorrecto(nombre):
            self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setContraseña(self,contraseña):
        if self.esContraseñaCorrecta(contraseña):
            self.contraseña = contraseña

    def getContraseña(self):
        return self.contraseña

    def setPuntuacionMaxima(self, puntuacion):
        self.puntuacionMaxima = puntuacion
    
    def getPuntuacionMaxima(self):
        return self.puntuacionMaxima
