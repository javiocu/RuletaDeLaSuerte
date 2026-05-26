// Archivo qml para desplegar frontend o interfaz gráfica

import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 800
    height: 400
    visible: true
    title: "La ruleta de la suerte"
    color: "#004d40"
    property bool partidaIniciada: false // Propiedad para controlar el inicio

    Column {
        id: pantallaInicio
        visible: !partidaIniciada
        anchors.centerIn: parent
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
                id: textoPicture
                anchors.horizontalCenter: parent.horizontalCenter
                text: "NUEVO JUGADOR"
                font.pixelSize: 20
                color: "#d8be2d"
            }
        }

        TextField {
            id: introducirJugador
            anchors.horizontalCenter: parent.horizontalCenter
            focus: true
            onAccepted: {
                partidaBackend.anadir_jugador(text)
                text = ""
            }
        }

        Button {
            id: textoComenzarPartida
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
                color: "#ffffff"
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 25
                text: "Ya existe un jugador con ese nombre, por favor introduce otro jugador"
            }
        }
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
        Fila {
            id: fila1
            textoFila: fraseBackend.fila1_propi
        }
        // Fila 2
        Fila {
            id: fila2
            textoFila: fraseBackend.fila2_propi
            visible: fraseBackend.fila2_propi === "            " ? false : true
        }
        // Fila 3
        Fila {
            id: fila3
            textoFila: fraseBackend.fila3_propi
            visible: fraseBackend.fila3_propi === "            " ? false : true

        }
        // Fila 4
        Fila {
            id: fila4
            textoFila: fraseBackend.fila4_propi
            visible: fraseBackend.fila4_propi === "            " ? false : true
        }
    }
}

