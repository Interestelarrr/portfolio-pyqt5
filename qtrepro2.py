import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class AppRepro(QWidget):
    def __init__(self):
        super(AppRepro, self).__init__()
        self.ReWindow()

    def ReWindow(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("Reproductor de Musica")
        self.displaylabels()

    def displaylabels(self):
        texto = QLabel(self)
        texto.setText("Hola")
        texto.move(500, 15)

        image = r"C:\Users\drevenzz\Downloads\expro.png"
        try:
            with open(image):
                labelimage = QLabel(self)
                pixmap = QPixmap(image)
                labelimage.setPixmap(pixmap)
                labelimage.move(30, 30)
        except:
            print("No se encontro la imagen en la ruta especifica")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppRepro()
    window.show()
    sys.exit(app.exec_())
            

    