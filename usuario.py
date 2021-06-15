class Usuario:

    nombre = ""

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
