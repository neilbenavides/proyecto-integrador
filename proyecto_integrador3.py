import os
import readchar

def leer_tecla():
    numero_actual = 0

    while numero_actual <= 50:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Presiona la tecla 'n' para avanzar. Número actual: {numero_actual}")

        tecla = readchar.readkey()

        if tecla == "n":
          numero_actual += 1

leer_tecla()
