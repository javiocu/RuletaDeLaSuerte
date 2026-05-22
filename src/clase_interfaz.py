"""Módulo dedicado a la clase IterfazPanel que no permite generar frame en la
pantalla para poder dibujar diferente rectángulos en asociados a palabras."""

import tkinter as tk
from clase_frase import Frase

class InterfazPanel:
    """Clase para dibujar la interfaz del panel"""

    def __init__(self, texto_frase: str, ventana_panel: tk.Tk,) -> None:
        self.frase_juego = Frase(texto_frase)
        self.filas = self.frase_juego.separar_en_filas()
        self.ventana = ventana_panel
        # Se genera lo paneles para las filas
        self.lienzo1 = tk.Frame(self.ventana)
        self.lienzo2 = tk.Frame(self.ventana)
        self.lienzo3 = tk.Frame(self.ventana)
        self.lienzo4 = tk.Frame(self.ventana)
        # Se empaquetan las filas en los frames con pack
        self.lienzo1.pack()
        self.lienzo2.pack()
        self.lienzo3.pack()
        self.lienzo4.pack()