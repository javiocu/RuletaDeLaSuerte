import QtQuick
import QtQuick.Controls

Row {
    spacing: 40
    Column {
        id: pantallitaInicio
        spacing: 10
        Column {
            id: fotoInicio
            anchors.horizontalCenter: parent.horizontalCenter

            Image {
                id: pictureInicial
                anchors.horizontalCenter: parent.horizontalCenter
                source: "file:./src/foto_portada.jpg"
                width: 400
                height: 300
                fillMode: Image.PreserveAspectFit // Preservar tamaño foto
            }

            Text {
                id: textoNuevoJugador
                anchors.horizontalCenter: parent.horizontalCenter
                text: "NUEVO JUGADOR"
                font.pixelSize: 30
                color: "#000000"
            }
        }

        TextField {
            id: casillaIntroducirJugador
            anchors.horizontalCenter: parent.horizontalCenter
            focus: true
            onAccepted: {
                partidaBackend.anadir_jugador(text)
                text = ""
            }
        }

        Button {
            id: botonComenzarPartida
            anchors.horizontalCenter: parent.horizontalCenter
            text: "¡Comenzar partida!"
            onClicked: {
                partidaIniciada = true
                tableroJuego.forceActiveFocus() // Cuando empieza la partida pongo el foco del teclado en la columna con el tablero.
            }
        }

        Column {
            id: mensajeJugadorExistente
            anchors.horizontalCenter: parent.horizontalCenter
            visible: partidaBackend.aviso_jugador_existente

            Text {
                color: "#000000"
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 25
                text: "Ya existe un jugador con ese nombre, por favor introduce otro jugador"
            }
        }
    }
    
    MarcadorPuntuacion {
        id: marcadorInicio
        anchors.verticalCenter: parent.verticalCenter
    }
}

