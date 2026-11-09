frase = " Los ojos de Ana Maria "

tamaño_fila = 12

def __separar_palabras__(frase:str):
    """Separa las frases en palabras individuales, devuelve lista.

    Args:
        frase (str): Frase tipo string para separar

    Returns:
        frases (list): Lista de palabras individuales.
    """
    frases = frase.lower().split()
    return frases


def frase_cabe(frase:str):
    """Comprueba si una frase entra en en el tablero antes de mandarla a la aplicación.

    Args:
        frase (str): _description_

    Returns:
        bool: Indica True o False si la frase cabe o no cabe en las cuatro filas.
    """
    frase = frase.lower().strip()
    palabras = __separar_palabras__(frase)
    if len(frase) > 48:
        return False
    fila1 = []
    fila2 = []
    fila3 = []
    fila4 = []
    for palabra in palabras:
        if len(palabra) > 12:
            return False
        elif tamaño_fila >= len(fila1) + len(palabra) + (1 if fila1 else 0): # Comprobar si cabe en la primera fila
            fila1.append(palabra)
        elif tamaño_fila >= len(fila2) + len(palabra) + (1 if fila2 else 0):
            fila2.append(palabra)
        elif tamaño_fila >= len(fila3) + len(palabra) + (1 if fila3 else 0):
            fila3.append(palabra)
        elif tamaño_fila >= len(fila4) + len(palabra) + (1 if fila4 else 0):
            fila4.append(palabra)
        else:
            return False
    return True


if __name__ == "__main__":
   
    print(frase_cabe(frase))