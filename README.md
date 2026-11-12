# La Ruleta de la Suerte 🎡

Proyecto desarrollado en Python con **PyQt6** y **QML (Qt Quick)** para recrear una versión del concurso de televisión *La Ruleta de la Suerte*.

La aplicación busca ofrecer una interfaz gráfica moderna y animada, manteniendo una separación clara entre la lógica del juego (Python) y la presentación visual (QML).

---

## 🚀 Funcionalidades actuales

- **Pantalla de inicio:** permite registrar jugadores antes de comenzar la partida.
- **Registro de jugadores:** se pueden añadir varios jugadores de forma consecutiva desde la interfaz gráfica.
- **Control de duplicados:** el backend comprueba si el nombre ya existe y muestra un aviso visual en pantalla.
- **Marcador de puntuación:** muestra los jugadores registrados y el dinero acumulado por cada uno.
- **Tablero de frase:** la frase se divide automáticamente en hasta cuatro filas, respetando el límite de caracteres por línea.
- **Descubrimiento de letras:** al pulsar una tecla durante la partida, se comprueba si la letra está en la frase y se actualiza el tablero.
- **Gestión del foco:** al pulsar “¡Comenzar partida!”, el foco del teclado pasa automáticamente al tablero.
- **Compatibilidad con Windows:** se utiliza el estilo visual *Fusion* de Qt Quick Controls para evitar problemas de renderizado de texto en Windows 11.

---

## 🛠️ Arquitectura del proyecto

El proyecto se organiza en dos capas principales: la lógica del juego en Python y la interfaz gráfica en QML.

| Archivo | Responsabilidad |
|---|---|
| `src/main.py` | Punto de entrada. Configura Qt, crea las instancias de `Frase` y `Partida`, las expone a QML y carga la interfaz. |
| `src/clase_frase.py` | Gestiona la frase oculta: separación en palabras, distribución en filas, letras descubiertas y actualización del tablero. |
| `src/clase_jugador_partida.py` | Gestiona los jugadores, el registro, la detección de nombres duplicados, el marcador y la lógica básica de la partida. |
| `src/main.qml` | Ventana principal. Controla la transición entre la pantalla de inicio y el tablero, además de capturar las teclas pulsadas. |
| `src/PantallaInicio.qml` | Pantalla de registro de jugadores, botón de inicio y aviso de jugador duplicado. |
| `src/MarcadorPuntuacion.qml` | Marcador con el nombre y el dinero de cada jugador. |
| `src/FilaFrase.qml` | Componente reutilizable que representa una fila del tablero, mostrando las letras descubiertas y ocultando las pendientes. |

---

## 📁 Estructura del proyecto

```text
.
├── src/
│   ├── main.py
│   ├── clase_frase.py
│   ├── clase_jugador_partida.py
│   ├── main.qml
│   ├── PantallaInicio.qml
│   ├── MarcadorPuntuacion.qml
│   ├── FilaFrase.qml
│   ├── foto_ruleta_portada.png
│   └── portatapeles.py
├── requerimientos.txt
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10 o superior.
- PyQt6.
- Entorno virtual recomendado.

### Instalación

Desde la raíz del proyecto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requerimientos.txt
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requerimientos.txt
```

---

## ▶️ Ejecución

Desde la raíz del proyecto, con el entorno virtual activado:

```bash
python src/main.py
```

La aplicación abrirá una ventana donde podrás registrar jugadores y, posteriormente, comenzar la partida.

---

## 🧩 Funcionalidades previstas

- Girar la ruleta y obtener premios, penalizaciones o quiebra.
- Sistema de turnos entre jugadores.
- Compra de vocales y resolución de la frase.
- Carga de frases desde un archivo externo.
- Validación más completa de nombres y entradas del usuario.
- Persistencia opcional de resultados o historial de partidas.
- Mejoras visuales, animaciones y personalización del regalo.

---

## 🎯 Estado del proyecto

Actualmente, el proyecto cuenta con una base funcional de registro de jugadores, marcador y tablero de frase con descubrimiento de letras. La siguiente fase natural es añadir la lógica de turnos y la ruleta.
