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
        Column {
            id: marcador
            Row {
                id: tituloMarcador
                Rectangle {
                    width: 400
                    height: 50
                    border.color: "black"
                    border.width: 2
                    topLeftRadius: 20
                    topRightRadius: 20
                    Text {
                        anchors.centerIn: parent
                        text: "MARCADOR"
                        font.pixelSize: 20
                    }
                }
            }
            Column {
                id: filas
                Column {
                    width: 400
                    height: 50
                    Text {
                        anchors.centerIn: tituloMarcador
                        text: "JUGADOR"
                        font.pixelSize: 20
                    }
                }
            }
        }
    }
}



