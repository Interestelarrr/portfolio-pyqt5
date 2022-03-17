from cProfile import label
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys

class buscadorPelis(QWidget):
    def __init__(self):
        super(buscadorPelis, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,340,200)
        self.setWindowTitle("Buscador de peliculas")
        self.mostrarBuscador()

    def mostrarBuscador(self):
        labelCatalogo = QLabel("Catalogo de Peliculas", self)
        labelCatalogo.move(20,20)
        labelCatalogo.setFont(QFont("Arial", 20))

        labelPelicula = QLabel("Ingrese la pelicula", self)
        labelPelicula.move(20,60)

        labelNombre = QLabel("Pelicula", self)
        labelNombre.move(20,90)

        self.peliculaInput = QLineEdit(self)
        self.peliculaInput.setPlaceholderText("Nombre de la pelicula")
        self.peliculaInput.move(80,90)
        self.peliculaInput.resize(240,20)

        self.boton = QPushButton("Buscar", self)
        self.boton.move(95,130)
        self.boton.resize(150,40)
        self.boton.clicked.connect(self.mostrarBusqueda)

    def mostrarBusqueda(self):
        try:
            with open("perfil\pelis.txt") as f:
                pelis = [content.rstrip("\n") for content in f]
        except FileNotFoundError:
            print("No se encontro el archivo")

        if self.peliculaInput.text() in pelis:
            QMessageBox().information(self, "Pelicula encontrada", "Pelicula encontrada en el Catalogo", QMessageBox.Ok)
        else:
            pelicula_no_encontrada = QMessageBox.question(self, "Pelicula no encontrada", "Pelicula no encontrada en el catalogo. \nDesea seguir", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if pelicula_no_encontrada == QMessageBox.No:
                print("Se cerrara el buscador")
                self.close()
            else:
                pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = buscadorPelis()
    window.show()
    sys.exit(app.exec_())