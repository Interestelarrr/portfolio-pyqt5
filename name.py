from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5 import QtCore
import sys

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.inicioUi()
    
    def inicioUi(self):
        self.setGeometry(100,100,400,200)
        self.setWindowTitle("Widget Name QLine")
        self.mostrarWidgets()

    def mostrarWidgets(self):
        QLabel("Escribe tu nombre", self).move(100,10)
        nombre = QLabel(self)
        nombre.move(70,50)

        self.nombreInput = QLineEdit(self)
        self.nombreInput.move(130,50)
        self.nombreInput.resize(200,20)
        self.nombreInput.setAlignment(QtCore.Qt.AlignLeft)

        self.boton = QPushButton(self)
        self.boton.move(160,110)
        self.boton.setText("Limpiar")
        self.boton.clicked.connect(self.limpiarInput)

    def limpiarInput(self):
        sender = self.sender()
        if sender.text() == 'Limpiar':
            self.nombreInput.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())