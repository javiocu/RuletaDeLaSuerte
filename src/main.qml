// Archivo qml para desplegar frontend o interfaz gráfica

import QtQuick
import QtQuick.Window


Window {
    width: 800
    height: 400
    visible: true
    title: "La ruleta de la suerte"
    color: "#004d40"
    Column {
        anchors.centerIn: parent
        spacing: 10
        // Fila 1
        Fila {
            textoFila: fraseBackend.fila1_propi
        }
        // Fila 2
        Fila {
            textoFila: fraseBackend.fila2_propi
            visible: fraseBackend.fila2_propi === "            " ? false : true
            }
        // Fila 3
        Fila {
            textoFila: fraseBackend.fila3_propi
            visible: fraseBackend.fila3_propi === "            " ? false : true

        }
        // Fila 4
        Fila {
            textoFila: fraseBackend.fila4_propi
            visible: fraseBackend.fila4_propi === "            " ? false : true
        }
    }
}
