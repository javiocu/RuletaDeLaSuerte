"""Módulo para procesar las frases que se quieran adivinar
Entrará una frase que debe separarse en filas. Puedo crear una clase que se
tenga diferentes características para las frases"""

class Frase:
    """Clase asociada a las frases. Servirá para tratarlas y procesarlas"""

    numero_total_caracteres = 12                    # Variables de clase:
                                                    # Número total de caracteres por fila
    def __init__(self, texto_frase:str) -> None:
        self.texto_frase = texto_frase              # Variables de instancia: 
        self.longitud = len(texto_frase)            # - la frase en sí - Su longitud
        self.numero_filas = 1
        self.lista_palabras = self.__separar_palabras__()

        self.fila1 = []
        self.fila2 = []
        self.fila3 = []
        self.fila4 = []

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

        partes_dic = {"fila1":self.fila1,
                      "fila2":self.fila2, 
                      "fila3":self.fila3, 
                      "fila4":self.fila4}
        return partes_dic
