"""Módulo para procesar las frases que se quieran adivinar
Entrará una frase que debe separarse en filas. Puedo crear una clase que se
tenga diferentes características para las frases"""

from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal

class Frase(QObject):
    """Clase asociada a las frases. Servirá para tratarlas y procesarlas"""

    numero_total_caracteres = 12                    # Variables de clase:
                                                    # Número total de caracteres por fila
    def __init__(self, texto_frase:str) -> None:
        super().__init__()                          # Llamo a super para tener los métodos del padre QObject
        
        self.texto_frase = texto_frase              # Variables de instancia: 
        self.longitud = len(texto_frase)            # - la frase en sí - Su longitud
        self.numero_filas = 1
        self.lista_palabras = self.__separar_palabras__()
        
        self.fila1 = []
        self.fila2 = []
        self.fila3 = []
        self.fila4 = []
        
        self.filas = self.separar_en_filas()

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

    # Voy a usar el método center para rellenar los espacios pero este algoritmo funcionaría:
    
    # def __rellenar_espacios__(self, fila) -> str:
    #     espacios_necesarios = 0
    #     if len(fila) == 12:
    #         return fila
    #     else:
    #         espacios_necesarios = 12 - len(fila)

    #     if espacios_necesarios % 2 == 0:                    # Espacios necesarios son pares
    #         espacio_lado = int(espacios_necesarios / 2)     # Espacios a cada lado
    #     else:                                               # Espacios necesarios son impares
    #         espacio_lado = int((espacios_necesarios - 1)  / 2)
    #         fila = fila + " "                               # Añado un espacio de base a la derecha

    #     for i in range(espacio_lado):                       # Bucle para añadir espacios
    #         fila = " " + fila
    #         fila = fila + " "
    #     return fila

    @pyqtProperty(str)
    def fila1_propi(self) -> str:
        """Propiedad para qml que envía la fila 1"""
        return (" ").join(self.fila1).center(12, " ")

    @pyqtProperty(str)
    def fila2_propi(self) -> str:
        """Propiedad para qml que envía la fila 2"""
        return (" ").join(self.fila2).center(12, " ")

    @pyqtProperty(str)
    def fila3_propi(self) -> str:
        """Propiedad para qml que envía la fila 3"""
        return (" ").join(self.fila3).center(12, " ")

    @pyqtProperty(str)
    def fila4_propi(self) -> str:
        """Propiedad para qml que envía la fila 4"""
        return (" ").join(self.fila4).center(12, " ")
    

if __name__ == "__main__":
    prueba = Frase("Prueba ")
    print(len(prueba.fila1_propi()))

