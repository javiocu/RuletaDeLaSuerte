// Archivo qml para desplegar frontend o interfaz gráfica

import QtQuick
import QtQuick.Window


Window {
    width: 800
    height: 400
    visible: true
    title: "La ruleta de la suerte"
    color: "#004d40"
    Row {
        anchors.centerIn: parent
        Repeater {
            model: fraseBackend.fila1_propi.split("")
            Rectangle {
                width: 50
                height: 50
                color: "#ffffff"
                border.color: "#000000"
                border.width: 2

                Text {
                    anchors.centerIn: parent // Pone la letra en el centro del rectángulo
                    text: modelData
                    font.pixelSize: 24
                }
            }

        }
    }
}
