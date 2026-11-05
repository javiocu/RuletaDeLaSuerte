frase = "Los ojos de Ana Maria"

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
    palabras = __separar_palabras__(frase)
    n_espacios = len(palabras) - 1
    if len(palabras) + n_espacios > 48:
        return False
    fila1 = []
    fila2 = []
    fila3 = []
    fila4 = []
    for palabra in palabras:
        if tamaño_fila >= len(fila1) + len(palabra) + (1 if fila1 else 0): # Comprobar si cabe en la primera fila
            fila1.append(palabra)
        elif tamaño_fila >= len(fila2) + len(palabra) + (1 if fila2 else 0):
            fila2.append(palabra)
        elif tamaño_fila >= len(fila3) + len(palabra) + (1 if fila3 else 0):
            fila3.append(palabra)
        elif tamaño_fila >= len(fila4) + len(palabra) + (1 if fila4 else 0):
            fila4.append(palabra)
        else:
            return False
    return fila1


if __name__ == "__main__":
    
    print(frase_cabe(frase))