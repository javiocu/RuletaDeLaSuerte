# Voy a usar el método center para rellenar los espacios pero este algoritmo funcionaría:

def __rellenar_espacios__(self, fila) -> str:
    espacios_necesarios = 0
    if len(fila) == 12:
        return fila
    else:
        espacios_necesarios = 12 - len(fila)

    if espacios_necesarios % 2 == 0:                    # Espacios necesarios son pares
        espacio_lado = int(espacios_necesarios / 2)     # Espacios a cada lado
    else:                                               # Espacios necesarios son impares
        espacio_lado = int((espacios_necesarios - 1)  / 2)
        fila = fila + " "                               # Añado un espacio de base a la derecha

    for i in range(espacio_lado):                       # Bucle para añadir espacios
        fila = " " + fila
        fila = fila + " "
    return fila
