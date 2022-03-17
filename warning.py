from cgitb import text
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys

class textWarning(QWidget):
    def __init__(self):
        super(textWarning, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Buscador de peliculas")
        self.displayWidget()

    def displayWidget(self):
        self.boton = QPushButton("Presiona", self)
        self.boton.move(80, 100)
        self.boton.clicked.connect(self.cuadroWarning)

    def cuadroWarning(self):
        cuadro = QMessageBox(self)
        cuadro.setIcon(QMessageBox.Warning)
        cuadro.setWindowTitle("Advertencia")
        cuadro.setText("Cuadro de dialogo")
        cuadro.setInformativeText("Texto de Advertencia")
        cuadro.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        cuadro.setDefaultButton(QMessageBox.Cancel)
        cuadro.setDetailedText("Cuadro de Detalles")
        boton = cuadro.exec_()
        if boton == QMessageBox.Save:
            print("Se ha usado el boton de Save")
        elif boton == QMessageBox.Cancel:
            print("Se ha usado el boton de Cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = textWarning()
    window.show()
    sys.exit(app.exec_())