import os
import readchar

# Definir el tamaño del laberinto

mapa_laberinto = "..#########\n#...#...#.#\n#.#.###.#.#\n#.#.......#\n#.#.#.#.###\n#.#.#.#...#\n#.#.#.#.#.#\n#.#.#.#.#.#\n###.#.#.#.#\n###.###.#..\n##########."

# Crear el laberinto

def matriz_mapa_laberinto(mapa_laberinto):
    matriz = []

    for elementos in mapa_laberinto.split("\n"):
        fila = list(elementos)
        matriz.append(fila)
    return matriz

matriz_mapa = matriz_mapa_laberinto(mapa_laberinto)

# Función para dibujar el laberinto en la pantalla

def imprimir_mapa_laberinto():
    os.system('cls' if os.name == 'nt' else 'clear')
    for matriz_caracteres in matriz_mapa:
        print("".join(matriz_caracteres))

# Bucle principal del juego

def main_loop(): 

    py, px = (0,0)
    matriz_mapa[py][px] = "P"

    while True:

        imprimir_mapa_laberinto()
        nuevo_px, nuevo_py = px, py
        key = readchar.readkey()

        if key == readchar.key.UP:
            nuevo_py -= 1
        elif key == readchar.key.DOWN:
            nuevo_py += 1
        elif key == readchar.key.LEFT:
            nuevo_px -= 1
        elif key == readchar.key.RIGHT:
            nuevo_px += 1
        
        if 0 <= nuevo_py < len(matriz_mapa) and 0 <= nuevo_px < len(matriz_mapa[0]) and matriz_mapa[nuevo_py][nuevo_px] != '#':
            matriz_mapa[py][px] = "."
            px, py = nuevo_px, nuevo_py
            matriz_mapa[nuevo_py][nuevo_px] = "P"

            if matriz_mapa[nuevo_py][nuevo_px] == '#':
                matriz_mapa[nuevo_py][nuevo_px] = "#"

        if nuevo_py == 11 and nuevo_px == 10 :         
            print ("¡Lo lograste! Felicidades")
            break     
main_loop()
