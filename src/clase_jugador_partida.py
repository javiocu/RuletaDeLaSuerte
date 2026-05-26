"""Módulo que almacena la clase jugador y partida, para manejar la entidad de jugadores"""
from PyQt6.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

class Jugador():
    """Clase orientada a describir Jugadores"""

    def __init__(self, nombre: str) -> None:
        self.name = nombre
        # if nombre == "lulu":
        #     self.dinero = 3
        # elif nombre == "juan":
        #     self.dinero = 2
        # else:
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
            jugador = Jugador(nombre_nuevo)
            for ya_inscrito in self.lista_jugadores:
                if ya_inscrito.name == jugador.name:
                    self.existe = True
                    self.jugador_exitente.emit()
                    return None
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

    def __ordenar_jugadores__(self) -> dict:
        """Método privado que ordena jugadores en función del dinero que lleven.

        Returns:
            list: Lista ordenada de jugadores en función del dinero que acumulen
        """
        diccionario_ordenado = {}
        for jugador in self.lista_jugadores:
            diccionario_ordenado[jugador.name] = int(jugador.dinero)
        diccionario_ordenado = sorted(diccionario_ordenado.items(), reverse=True, key=lambda key: key[1])
        return diccionario_ordenado



if __name__ == "__main__":
    partida1 = Partida()
    partida1.anadir_jugador("Juan")
    partida1.anadir_jugador("Javi")
    partida1.anadir_jugador("Lulu")
    print(partida1.__ordenar_jugadores__())
