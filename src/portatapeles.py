import QtQuick
import QtQuick.Controls

# Este es el lienzo principal de la fila
Rectangle {
    id: contenedorFila
    width: 400
    height: 60
    color: "#006644" # Un color verde tipo tablero de concurso

    # Dentro del lienzo, dibujamos una casilla para una letra
    Rectangle {
        id: casillaLetra
        width: 40
        height: 50
        color: "white" # Casilla blanca
        radius: 4      # Bordes un poco redondeados
        
        # Centramos la casilla verticalmente en la fila
        anchors.verticalCenter: parent.verticalCenter
        x: 10 # Posición horizontal manual por ahora

        # Texto que irá dentro de la casilla
        Text {
            text: "A"
            font.pixelSize: 24
            font.bold: true
            anchors.centerIn: parent # Centrado perfecto dentro del rectángulo blanco
            color: "black"
        }
    }
}