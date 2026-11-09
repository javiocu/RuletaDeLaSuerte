"""Módulo principal diseñado para ejecutar la aplicación"""

import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

from clase_frase import Frase
from clase_jugador_partida import Partida
import cargar_frases

import os
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Fusion" # Necesario para poder mostrar textos en windows. Estilo genérico.

def ruleta_suerte():
    # Arrancar aplicación y motor interno de qml
    app = QGuiApplication(sys.argv) # sys.argv para que coja los argumentos de la línea de comandos
    engine = QQmlApplicationEngine() # Creo instancia del motor de comunicación con qml para interpretar el archivo qml

    # Creo intancia de frase para cargar
    ruta_archivo = "src/listado_frases.json"
    frase_completa = cargar_frases.elegir_frase_json(ruta_archivo)
    frase_juego = Frase(frase_completa["frase"])
    partida = Partida()

    # Arranco instancias con archivos qml del espacio
    engine.rootContext().setContextProperty("fraseBackend", frase_juego)
    engine.rootContext().setContextProperty("partidaBackend", partida)

    # Cargo el archivo qml de interfaz gráfica
    engine.load("src/main.qml")

    # Si el archivo qml no se puede cargar, exiteo con error:
    # rootObjetcs devuelve los objetos creados por QQmlApplicationEngine.load() 
    if not engine.rootObjects():
        print("Error: Illo el archivo main.qml no existe o está vacío")
        sys.exit(-1) # -1 indicando error de ejecución

    # Arranco aplicación en bucle:
    sys.exit(app.exec())

if __name__ == "__main__":
    ruleta_suerte()
