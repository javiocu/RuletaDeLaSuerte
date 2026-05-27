// Archivo qml para desplegar frontend o interfaz gráfica

import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 800
    height: 400
    visible: true
    title: "La ruleta de la suerte"
    color: "#07d4db"
    property bool partidaIniciada: false // Propiedad para controlar el inicio

    Column {
        id: pantallaInicio
        visible: !partidaIniciada
        anchors.centerIn: parent
        spacing: 10
        PantallaInicio {
            // Pantalla inicio en otro archivo para facilitar la lectura
        }
    }

    MarcadorPuntuación {

    }

    Column {
        id: tableroJuego
        focus: partidaIniciada
        visible: partidaIniciada
        Keys.onPressed: (event) => {
            fraseBackend.esta_letra_dicha(event.text.toUpperCase())
        }
        anchors.centerIn: parent
        spacing: 10
        // Fila 1
        FilaFrase {
            id: fila1
            textoFila: fraseBackend.fila1_propi
        }
        // Fila 2
        FilaFrase {
            id: fila2
            textoFila: fraseBackend.fila2_propi
            visible: fraseBackend.fila2_propi === "            " ? false : true
        }
        // Fila 3
        FilaFrase {
            id: fila3
            textoFila: fraseBackend.fila3_propi
            visible: fraseBackend.fila3_propi === "            " ? false : true

        }
        // Fila 4
        FilaFrase {
            id: fila4
            textoFila: fraseBackend.fila4_propi
            visible: fraseBackend.fila4_propi === "            " ? false : true
        }
    }
}

