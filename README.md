# La Ruleta de la Suerte 🎡

Proyecto desarrollado en Python utilizando **PyQt6** y **QML (Qt Quick)** para recrear el concurso de televisión. La aplicación contará con una interfaz gráfica moderna, animada y una separación limpia entre la lógica del juego y el diseño visual.

---

## 🚀 Características potenciales

- **Frontend dinámico:** Diseñado completamente en QML con transiciones fluidas entre pantallas.
- **Sistema de Registro:** Permite añadir múltiples jugadores de forma consecutiva desde la interfaz gráfica.
- **Control de Duplicados:** El backend valida en tiempo real que no se introduzcan jugadores con el mismo nombre, mostrando un aviso visual interactivo.
- **Gestión Intuitiva de Foco:** Transición automática del foco del teclado desde el campo de texto al tablero de juego al iniciar la partida.
- **Multiplataforma Robusta:** Configurado específicamente para evitar fallos de renderizado en Windows 11 utilizando el estilo visual *Fusion*.

---

## 🛠️ Arquitectura del Proyecto

El proyecto sigue una arquitectura:

- **`src/main.py`**: El motor principal de la aplicación. Configura el entorno de Qt, instancia las clases de Python y las conecta al contexto de QML.
- **`src/clase_frase.py`**: Gestiona la frase oculta del tablero, el estado de las letras (adivinadas/ocultas) y la distribución en las 4 filas reglamentarias.
- **`src/clase_jugador_partida.py`**: Maneja la entidad de los jugadores (nombre, puntuación/dinero) y la lógica de la partida (control de turnos y validación de jugadores).
- **`src/main.qml`**: Define toda la interfaz gráfica, botones, campos de texto y la lógica de eventos del teclado (`Keys.onPressed`).


### Dependencias
Tener instalado Python 3.10. Usar pip en entorno virtual para intalar requisitos con archivo 'requerimientos.txt'

```bash
pip install -r requerimientos.txt