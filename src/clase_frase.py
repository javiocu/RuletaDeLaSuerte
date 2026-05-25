"""Módulo para procesar las frases que se quieran adivinar
Entrará una frase que debe separarse en filas. Puedo crear una clase que se
tenga diferentes características para las frases"""

from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

class Frase(QObject):
    """Clase asociada a las frases. Servirá para tratarlas y procesarlas"""

    numero_total_caracteres = 12                    # Variables de clase
    actualizar_tablero = pyqtSignal()

    def __init__(self, texto_frase:str) -> None:
        super().__init__()                          # Llamo a super para tener los métodos del padre QObject

        self.texto_frase = texto_frase.upper()      # Variables de instancia
        self.longitud = len(texto_frase)
        self.lista_palabras = self.__separar_palabras__()
        self.letras_dichas = set()

        self.fila1 = []
        self.fila2 = []
        self.fila3 = []
        self.fila4 = []

        self.separar_en_filas()

    def __separar_palabras__(self) -> list:
        """Método que separa las palabras, generando una lista

        Returns:
            list: lista de palabras
        """
        lista_palabras = self.texto_frase.split(" ")
        return lista_palabras

    def __sacar_caracteres__(self, lista:list) -> int:
        """Método que calcula el número de caracteres totales de una lista de 
        palabras que se le pase. Se usará principalmente para contar los
        caracteres en las filas.

        Args:
            lista (list): Lista de palabras para contar lo caracteres totales

        Returns:
            int: Número total de caracteres de la lista de palabras
        """
        caracteres_totales = 0
        for palabra in lista:
            caracteres_totales += len(palabra)
        return caracteres_totales

    def separar_en_filas(self) -> dict:
        """Método de clase que separa la frase de entrada en diferentes filas.

        Returns:
            dict: lista con hasta cuatro filas de frases que caben en la pantalla
        """
        lista_palabras = self.__separar_palabras__()
        try:
            for palabra in lista_palabras:
                if len(self.fila1)- 1 + self.__sacar_caracteres__(self.fila1) + len(palabra) <= self.numero_total_caracteres:
                    self.fila1.append(palabra)
                elif len(self.fila2) - 1 + self.__sacar_caracteres__(self.fila2) + len(palabra) <= self.numero_total_caracteres:
                    self.fila2.append(palabra)
                elif len(self.fila3) - 1 + self.__sacar_caracteres__(self.fila3) + len(palabra) <= self.numero_total_caracteres:
                    self.fila3.append(palabra)
                elif len(self.fila4) - 1 + self.__sacar_caracteres__(self.fila4) + len(palabra) <= self.numero_total_caracteres:
                    self.fila4.append(palabra)
                else:
                    raise ValueError
        except ValueError as value_er:
            print(f"{value_er}: Illo la frase no cabe máquina, prueba otra")

        self.partes_dic = {"fila1":self.fila1,
                      "fila2":self.fila2, 
                      "fila3":self.fila3, 
                      "fila4":self.fila4}

    def __enmascarar_fila__(self, fila: list) -> str:
        """Toma una fila, la centra y oculta las letras no dichas."""
        fila_original = (" ").join(fila).center(12, " ")
        resultado = ""
        for l in fila_original:
            if l in self.letras_dichas:
                resultado += l
            elif l == " ":
                resultado += "_"
            else:
                resultado += " "
        return resultado

    @pyqtProperty(str, notify = actualizar_tablero)
    def fila1_propi(self) -> str:
        """Propiedad para qml que envía la fila 1"""
        return self.__enmascarar_fila__(self.fila1)

    @pyqtProperty(str, notify = actualizar_tablero)
    def fila2_propi(self) -> str:
        """Propiedad para qml que envía la fila 2"""
        return self.__enmascarar_fila__(self.fila2)

    @pyqtProperty(str, notify = actualizar_tablero)
    def fila3_propi(self) -> str:
        """Propiedad para qml que envía la fila 3"""
        return self.__enmascarar_fila__(self.fila3)

    @pyqtProperty(str, notify = actualizar_tablero)
    def fila4_propi(self) -> str:
        """Propiedad para qml que envía la fila 4"""
        return self.__enmascarar_fila__(self.fila4)

    # Establecer un set para acumular letras únicas y que no se repitan
    @pyqtSlot(str, result= bool)
    def esta_letra_dicha(self, letra: str) -> bool | None:
        """Método activo para que el usuario intdroduzca letras a comprobar

        Args:
            letra (str): Letra que se quiere comprobar

        Returns:
            str | None: Devuelve la letra si la letra no e ha dicho
        """
        if not letra.isalpha():
            return False
        elif letra in self.letras_dichas:
            print(f"La letra {letra} ya se ha dicho")
            return False
        else:
            print(f"¡La letra {letra} es válida!")
            self.letras_dichas.add(letra)
            self.actualizar_tablero.emit()
            return True



if __name__ == "__main__":
    prueba = Frase("La ruleta de la suerte")

