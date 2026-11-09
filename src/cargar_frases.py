import json
from pathlib import Path
import random


def elegir_frase_json(ruta_json:str):
    try:
        texto = Path(ruta_json).read_text()
    except FileNotFoundError:
        return f"ERROR ARCHIVO: No existe el archivo en el path esperado: {ruta_json}"
    try:
        lista_frases = json.loads(texto)
    except json.decoder.JSONDecodeError:
        return "ERROR DE FORMATO: El archivo no tiene un formato tipo json."
    frase_completa_final = ""
    # Cojo una frase aleatoria
    if hay_frase_valida(lista_frases):
        while not frase_completa_final:
            frase_completa_actual = lista_frases[random.choice(range(len(lista_frases)))]
            if frase_cabe(frase_completa_actual["frase"]):
                frase_completa_final = frase_completa_actual
                return frase_completa_final
    else:
        print("No hay ninguna frase válida en la lista json.")
        return False
    

def hay_frase_valida(lista_frases:list) -> bool:
    for frase_completa in lista_frases:
        if frase_cabe(frase_completa["frase"]):
            return True
    return False


def separar_palabras(frase:str):
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
    tamaño_fila = 12
    palabras = separar_palabras(frase)
    if frase == "":
        return False
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
    print(frase_cabe("   "))
    print(frase_cabe(""))
    print(frase_cabe("Hola bueas"))
    print(frase_cabe("Extraordinariamente"))
    print(frase_cabe("Qué crees que ocurrirá con esa quinta frase: fallará por longitud total, por no caber en las filas, o por ambas razones"))
    print(elegir_frase_json("src/listado_frases.json"))