from cmath import exp
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap
import sys

class PerfilUsuario(QWidget):
    def __init__(self):
        super(PerfilUsuario, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,300,440)
        self.setWindowTitle("Perfil del Usuario")
        self.mostrarImagenes()
        self.mostrarLabels()

    def mostrarImagenes(self):
        fotoPerfil = r"perfil/profile_image.png"
        fotoDeFondo = r"perfil/skyblue.jpg"

        try:
            with open(fotoDeFondo):
                labelFondo = QLabel(self)
                pixmap = QPixmap(fotoDeFondo)
                labelFondo.setPixmap(pixmap)
        except FileNotFoundError:
            print("No esta disponible la imagen en este Directorio")
        
        try:
            with open(fotoPerfil):
                labelPerfil = QLabel(self)
                pixmap = QPixmap(fotoPerfil)
                labelPerfil.setPixmap(pixmap)
                labelPerfil.move(100,25)
        except FileNotFoundError:
            print("No esta disponible la imagen en este Directorio")

    def mostrarLabels(self):
        nombreDeUsuario = QLabel(self)
        nombreDeUsuario.setText("drevenzz")
        nombreDeUsuario.move(100,155)
        nombreDeUsuario.setFont(QFont("Arial", 17))

        biografiaTitulo = QLabel(self)
        biografiaTitulo.setText("Biografia")
        biografiaTitulo.move(15, 185)
        biografiaTitulo.setFont(QFont("Arial", 17))

        biografia = QLabel(self)
        biografia.setText("Soy un desarollador con dos años de experiencia.")
        biografia.move(15, 220)
        biografia.setWordWrap(True)
        
        skillsTitulo = QLabel(self)
        skillsTitulo.setText("Skills")
        skillsTitulo.move(15, 260)
        skillsTitulo.setFont(QFont("Arial", 17))

        skills = QLabel(self)
        skills.setText("Python")
        skills.move(15, 290)
        skills.setWordWrap(True)

        experienciaTitulo = QLabel(self)
        experienciaTitulo.setText("Experiencia")
        experienciaTitulo.move(15, 320)
        experienciaTitulo.setFont(QFont("Arial", 17))

        experienciaCAT = QLabel(self)
        experienciaCAT.setText("AminoCAT Libreria de Python para AminoApps.com")
        experienciaCAT.move(15, 350)
        experienciaCAT.setFont(QFont("Arial", 8))

        drevenzzBot = QLabel(self)
        drevenzzBot.setText("Bot drevenzz con AminoCAT")
        drevenzzBot.move(15, 370)
        drevenzzBot.setFont(QFont("Arial", 8))

        devTime = QLabel(self)
        devTime.setText("Programando y Aprendiendo desde 12/20 hasta presente")
        devTime.move(15, 390)
        devTime.setFont(QFont("Arial", 8))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PerfilUsuario()
    window.show()
    sys.exit(app.exec_())
