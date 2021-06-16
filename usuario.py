class Usuario:

    nombre = ""
    puntuacionMaxima = 0

    def __init__(self, nombre=None, puntuacionMaxima=None):
        self.nombre = nombre
        self.puntuacionMaxima = puntuacionMaxima

    def __repr__(self):
        return repr((self.nombre, self.puntuacionMaxima))

    def esNombreUsuarioCorrecto(self,nombre):
        if len(nombre) <= 8:
            return True
        else:
            return False

    def setNombre(self,nombre):
        if self.esNombreUsuarioCorrecto(nombre):
            self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setPuntuacionMaxima(self, puntuacion):
        self.puntuacionMaxima = puntuacion
    
    def getPuntuacionMaxima(self):
        return self.puntuacionMaxima
