import readchar

print("Presiona cualquier tecla para empezar.")

while True:
    teclas = readchar.readkey()
    print("La tecla presionada es:", teclas)

    if teclas == readchar.key.UP:
        print("El programa ha sido detenido.")
        break
