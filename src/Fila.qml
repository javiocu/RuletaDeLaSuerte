import QtQuick


Row {
    property string textoFila: ""
    Repeater {
        model: textoFila.split("")
        Rectangle {
            width: 50
            height: 100
            color: modelData === " " ? "#0300b9" : "#ffffff"
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