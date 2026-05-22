# ProyectoSecreto

# 🤫 ProyectoSecreto

Este proyecto consiste en el desarrollo de una aplicación interactiva inspirada en el famoso concurso de televisión **"La Ruleta de la Suerte"**. Está diseñada especialmente para ejecutarse utilizando una pantalla táctil.

## 🌟 Características Principales

*   **Panel de Letras Ocultas:** Las palabras de la frase se organizan en filas de casillas rectangulares blancas que ocultan el texto.
*   **Modo de Búsqueda (Teclado):** Permite introducir una letra mediante el teclado. Si la letra existe en la frase, las casillas correspondientes se iluminarán en **color naranja** 🟧 como pista visual.
*   **Modo de Revelado (Táctil):** Tras iluminarse en naranja, el usuario puede tocar físicamente cada casilla seleccionada para "darle la vuelta" y revelar la letra oculta.
*   **Gestión de Frases:** Capacidad para procesar frases completas y dividirlas automáticamente en palabras.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3 🐍
*   **Interfaz Gráfica:** `tkinter` (Librería estándar de Python) 🖼️
*   **Entorno de Desarrollo:** VSCode sobre Windows 11 💻
*   **Control de Versiones:** Git alojado en una instancia local de Forgejo mediante Docker 🐳

## 🚀 Cómo Ejecutar el Proyecto

1. Clona este repositorio desde tu Forgejo local.
2. Abre la carpeta del proyecto en VSCode.
3. Ejecuta el archivo principal:
   
```bash
   python main.py