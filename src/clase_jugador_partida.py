"""Módulo que almacena la clase jugador y partida, para manejar la entidad de jugadores"""
from PyQt6.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
from random import randint
from clase_gajos import Gajo
import random

class Jugador():
    """Clase orientada a describir Jugadores"""

    def __init__(self, nombre: str) -> None:
        self.name = nombre
        self.dinero = 0



class Partida(QObject):
    """Clase orientada a organizar la partida"""
    jugador_exitente = pyqtSignal()
    turno_cambiado = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.lista_jugadores = []
        self.existe = False
        self.turno = 0
        self.ruleta = [
            Gajo("25€", 25, False, False),
            Gajo("50€", 50, False, False),
            Gajo("75€", 75, False, False),
            Gajo("100€", 100, False, False),
            Gajo("150€", 150, False, False),
            Gajo("200€", 200, False, False),
            Gajo("Quiebra", 0, True, False),
            Gajo("Pierde turno", 0, False, True)
        ]

    @pyqtSlot(str)
    def anadir_jugador(self, nombre: str) -> None:
        """Registra nuevos jugadores en la partida, dede el qml."""
        nombre_nuevo = nombre.lower().strip()
        self.existe = False
        if nombre_nuevo:
            jugador = Jugador(nombre_nuevo)
            for ya_inscrito in self.lista_jugadores:
                if ya_inscrito.name == jugador.name:
                    self.existe = True
                    self.jugador_exitente.emit()
                    return None
            self.lista_jugadores.append(jugador)
            self.jugador_exitente.emit()
            total = len(self.lista_jugadores)
            plural = "jugador"
            if total > 1:
                plural = "jugadores"
            print(f"¡{jugador.name.lower().capitalize()} se ha añadido al juego!, ya hay {total} {plural} en total.")

    @pyqtProperty(bool, notify = jugador_exitente)
    def aviso_jugador_existente(self) -> bool:
        """Devuelve valor true para mostrar mensaje de jugador existente"""
        return self.existe

    # Quiero poder poner una lista de jugadores en la pantalla con el dinero que
    # llevan ganado. Necesito una propiedad que se mande al front, y que sea
    # avisada por un Slot, cuando tenga que actualizarse
    @pyqtProperty(list, notify = jugador_exitente)
    def lista_nombres_pantalla(self) -> list:
        """Devuelve lista de jugadores, clase Jugador, en lista para 
        poder mandarlos a QML. Devuelve el dinero que llevan también.

        Returns:
            list: Lista de Jugadores
        """
        lista_mandar = []
        for jugador in self.lista_jugadores:
            nombre = str(jugador.name).capitalize()
            dinero = str(jugador.dinero)
            lista_mandar.append(f"{nombre}: {dinero}")
        return lista_mandar

    def __ordenar_jugadores__(self) -> list:
        """Método privado que ordena jugadores en función del dinero que lleven.

        Returns:
            list: Lista ordenada de jugadores en función del dinero que acumulen
        """
        diccionario_ordenado = {}
        for jugador in self.lista_jugadores:
            diccionario_ordenado[jugador.name] = int(jugador.dinero)
        lista_ordenada = sorted(diccionario_ordenado.items(), reverse=True, key=lambda dinero: dinero[1])
        return lista_ordenada

    @pyqtSlot()
    def seleccionar_turno_inicial(self) -> None:
        """Función para generar el turno inicial cuando se pulsa el botón comenzar 
        partida en la pantalla de inicio.
        """
        self.turno = randint(0, len(self.lista_jugadores)-1)
        self.turno_cambiado.emit()

    def _siguiente_turno(self) -> None:
        """Cambia el turno al siguiente índice.
        """
        self.turno = (self.turno + 1) % len(self.lista_jugadores)
        self.turno_cambiado.emit()

    def __tirar_ruleta(self) -> Gajo:
        gajo_tocado = random.choice(self.ruleta)
        return gajo_tocado

    def aplicar_gajo(gajo = Gajo) -> None:
        

if __name__ == "__main__":
    partida1 = Partida()
    # partida1.anadir_jugador("Juan")
    # partida1.anadir_jugador("Javi")
    # partida1.anadir_jugador("Lulu")
    # partida1.anadir_jugador("pepe")
    # # print(partida1.__ordenar_jugadores__())
    # turno = 0
    # for jugador in partida1.lista_jugadores:
    #     print(turno)
    #     print(jugador.name)
    print(partida1.tirar_ruleta().nombre)