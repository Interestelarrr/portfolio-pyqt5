from json.tool import main
from unicodedata import name
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
import sys

class WidgetBoton(QWidget):
    def __init__(self):
        super(WidgetBoton, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,300,150)
        self.setWindowTitle("Ventana con Boton")
        self.mostrarBotones()

    def mostrarBotones(self):
        label = QLabel(self)
        label.setText("Toca el boton")
        label.move(100,20)

        boton = QPushButton("Tocame", self)
        boton.move(105,50)
        boton.clicked.connect(self.botonConectado)

    def botonConectado(self):
        print("Cerrado, vuelva pronto")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetBoton()
    window.show()
    sys.exit(app.exec_())