from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class nuevoUsuario(QWidget):
    def __init__(self):
        super(nuevoUsuario, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Registro de Usuario")
        self.mostrarWidgets()

    def mostrarWidgets(self):
        userImage = r"LogeoyRegistro\NuevoUsuario.png"
        try:
            with open(userImage):
                eImagen = QLabel(self)
                pixmap = QPixmap(userImage)
                eImagen.setPixmap(pixmap)
                eImagen.move(175,80)
        except FileNotFoundError:
            print("No se ha podido encontrar la imagen en la ruta especificada")
        
        eLogin = QLabel("Crear una cuenta", self)
        eLogin.move(0,20)
        eLogin.setFont(QFont("Arial", 20))
        eLogin.resize(400,40)
        eLogin.setAlignment(Qt.AlignCenter)

        self.eNombre = QLabel("Nombre de Usuario", self)
        self.eNombre.move(30,180)

        self.nombreInput = QLineEdit(self)
        self.nombreInput.move(150,180)
        self.nombreInput.resize(200,20)

        self.ePassword = QLabel("Contraseña", self)
        self.ePassword.move(30,220)

        self.lnedPassword = QLineEdit(self)
        self.lnedPassword.setEchoMode(QLineEdit.Password)
        self.lnedPassword.move(150,220)
        self.lnedPassword.resize(200,20)
        
        self.confirmar = QLabel("Confirmar", self)
        self.confirmar.move(30,260)

        self.lnedConfirmar = QLineEdit(self)
        self.lnedConfirmar.setEchoMode(QLineEdit.Password)
        self.lnedConfirmar.move(150,260)
        self.lnedConfirmar.resize(200,20)

        self.botonRegistro = QPushButton("Registrarme", self)
        self.botonRegistro.resize(200,40)
        self.botonRegistro.move(100,310)
        self.botonRegistro.clicked.connect(self.registro)

    def registro(self):
        textoPassword = self.lnedPassword.text()
        confirmarPassword = self.lnedPassword.text()

        if textoPassword != confirmarPassword:
            QMessageBox.warning(self, "Mensaje de error", "Las contraseñas no coinciden, por favor pongalas correctamente.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open("usuario.txt", "a+") as f:
                f.write(self.nombreInput.text() + " ")
                f.write(textoPassword + "\n")
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = nuevoUsuario()
    window.show()
    sys.exit(app.exec_())