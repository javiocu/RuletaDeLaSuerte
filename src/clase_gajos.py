"""Módulo que almacena la clase gajos, para manejar la entidad de gajos de la ruleta"""
from PyQt6.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

class Gajo():
    def __init__(self,
                 nombre:str,
                 valor:int,
                 quiebra:bool,
                 pierde_turno:bool) -> None:
        # Defino atributos de instancia para los gajos
        self.nombre = nombre
        self.valor = valor
        self.quiebra = quiebra
        self.pierde_turno = pierde_turno
