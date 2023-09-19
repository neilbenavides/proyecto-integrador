import os
import readchar
import random
from functools import reduce

class Juego:
    def __init__(self, mapa_laberinto):
        self.mapa_laberinto = mapa_laberinto
        self.matriz_mapa = self.matriz_mapa_laberinto(self.mapa_laberinto)
        self.py, self.px = (0,0)
        self.matriz_mapa[self.py][self.px] = "P"

    def matriz_mapa_laberinto(self, mapa_laberinto):
        return list(map(list, mapa_laberinto))

    def imprimir_mapa_laberinto(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for matriz_caracteres in self.matriz_mapa:
            print("".join(matriz_caracteres))

    def main_loop(self):
        while True:
            self.imprimir_mapa_laberinto()
            nuevo_px, nuevo_py = self.px, self.py
            key = readchar.readkey()

            if key == readchar.key.UP:
                nuevo_py -= 1
            elif key == readchar.key.DOWN:
                nuevo_py += 1
            elif key == readchar.key.LEFT:
                nuevo_px -= 1
            elif key == readchar.key.RIGHT:
                nuevo_px += 1

            if 0 <= nuevo_py < len(self.matriz_mapa) and 0 <= nuevo_px < len(self.matriz_mapa[0]) and self.matriz_mapa[nuevo_py][nuevo_px] != '#':
                self.matriz_mapa[self.py][self.px] = "."
                self.px, self.py = nuevo_px, nuevo_py
                self.matriz_mapa[self.py][self.px] = "P"

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivos_mapa = random.choice(os.listdir(path_a_mapas))
        path_completo = f"{path_a_mapas}/{archivos_mapa}"
        mapa_laberinto = self.leer_mapa_laberinto(path_completo)
        super().__init__(mapa_laberinto)

    def leer_mapa_laberinto(self, archivos_mapa):
        with open(archivos_mapa, 'r') as archivo:
            lineas = archivo.readlines()
            coordenadas = map(lambda x: x.strip(), lineas)
        return list(coordenadas)

if __name__ == "__main__":
    juego = JuegoArchivo("mapas")
    juego.main_loop()
