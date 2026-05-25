"""Módulo que almacena la clase jugador, para manejar la entidad de jugadores"""
from PyQt6.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

class Jugador():
    """Clase orientada a describir Jugadores"""

    def __init__(self, nombre: str) -> None:
        self.name = nombre
        self.dinero = 0



class Partida(QObject):
    """Clase orientada a organizar la partida"""
    jugador_exitente = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.lista_jugadores = []
        self.existe = False
        
    @pyqtSlot(str)
    def anadir_jugador(self, nombre: str) -> None:
        """Registra nuevos jugadores en la partida, dede el qml."""
        nombre_nuevo = nombre.lower().strip()
        self.existe = False
        self.jugador_exitente.emit()
        if nombre_nuevo:
            for jugador in self.lista_jugadores:
                if nombre_nuevo == jugador.name:
                    self.existe = True
                    self.jugador_exitente.emit()
                    return
            jugador = Jugador(nombre)
            self.lista_jugadores.append(jugador)
            total = len(self.lista_jugadores)
            plural = "jugador"
            if total > 1:
                plural = "jugadores"
            print(f"¡{jugador.name.lower().capitalize()} se ha añadido al juego!, ya hay {total} {plural} en total.")

    @pyqtProperty(bool, notify = jugador_exitente)
    def aviso_jugador_existente(self) -> bool:
        """Devuelve valor true para mostrar mensaje de jugador existente"""
        return self.existe
