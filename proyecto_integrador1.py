# Proyecto Integrador Parte 1

print("¡Hola! ¿Cuál es tu nombre para que podamos conocernos mejor?")
nombre = input()
print(f"¡Hola, hola! {nombre}, Un aplauso virtual por unirte a nuestro juego.")


# Proyecto Integrador Parte 2

import readchar

print("Presiona cualquier tecla para empezar")

while True:
    teclas = readchar.readkey()
    print("La tecla presionada es:", teclas)

    if teclas == readchar.key.UP:
        print("El programa ha sido detenido.")
        break
    