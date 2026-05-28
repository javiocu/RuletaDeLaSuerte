import QtQuick
import QtQuick.Controls

// Propiedad para formar el tablero actualizado con las puntuaciones actualizadas
// Tiene que ser una tabla con dos columnas y tantas filas como jugadores

Column {
    Rectangle {
        id: rectanguloPadre
        width: 400
        height: 500
        border.color: "black"
        border.width: 2
        radius: 20
        color: "#ffffff9a"

        Column {
            id: marcador
            anchors.fill: parent
            spacing: 10
            // Título principal del marcador
            Row {
                Rectangle {
                    id: tituloMarcador
                    width: 400
                    height: 50
                    border.color: "black"
                    border.width: 2
                    topLeftRadius: 20
                    topRightRadius: 20
                    color: "#d8be2d"

                    Text {
                        anchors.centerIn: parent
                        text: "MARCADOR"
                        font.pixelSize: 20
                        font.bold: true
                        color: "#000000"
                    }
                }
            }
            // Encabezados de la tabla: Jugadores y Dinero
            Row {
                id: encabezadosMarcador
                spacing: 100
                anchors.horizontalCenter: parent.horizontalCenter

                Text {
                    anchors.horizontalCenter: parent
                    id: tituloJugador
                    text: "JUGADOR"
                    font.pixelSize: 16
                    font.bold: true
                    color: "#06aa5d"
                }
                Text {
                    anchors.horizontalCenter: parent
                    id: tituloDinero
                    text: "DINERO"
                    font.pixelSize: 16
                    font.bold: true
                    color: "#06aa5d"
                }
            }
            Repeater {
                model: partidaBackend.lista_nombres_pantalla // Método para traer la lista

                Row {
                    anchors.horizontalCenter: parent.horizontalCenter
                    spacing: 20
                    // Rectángulo para el nombre
                    Rectangle {
                        width: 140
                        height: 35
                        color: "#06aa5d"
                        border.color: "#000000"
                        border.width: 1
                        radius: 5

                        Text {
                            anchors.centerIn: parent
                            text: modelData.split(": ")[0]
                        }
                    }
                    // Rectángulo para el dinero
                    Rectangle {
                        width: 100
                        height: 35
                        color: "#06aa5d"
                        border.color: "#000000"
                        border.width: 1
                        radius: 5

                        Text {
                            anchors.centerIn: parent
                            text: modelData.split(": ")[1] + " €"
                            font.bold: true
                            color: "#d8be2d"
                        }
                    }
                    
                }
            }
        }
    }
}



