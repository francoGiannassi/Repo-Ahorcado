from ahorcado import Ahorcado
from usuario import Usuario

if __name__ == "__main__":
        ahorcado = Ahorcado()
        ahorcado.setPalabrasFaciles(["Ola","Rio","Casa","Via","Sol"])
        ahorcado.setPalabrasIntermedias(["Juego","Ahorcado","Visual","Estudio","Codigo"])
        ahorcado.setPalabrasDificiles(["Otorrinolaringologo","Desoxirribonucleico","Onomatopeya","Electroencefalografista"])
        ahorcado.setUsuarios([Usuario("Fran2",200),Usuario("Fran3",100),Usuario("Fran1",300)])
        print(ahorcado.getUsuarios())
        print(ahorcado.puestosOrdenadosRanking())
