from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from NuevoUsuario import nuevoUsuario
import sys

class loginRes(QWidget):
    def __init__(self):
        super(loginRes, self).__init__()
        self.inicioUi()
    
    def inicioUi(self):
        self.setGeometry(100,100,400,230)
        self.setWindowTitle("Formulario de Logeo")
        self.loginUi()

    def loginUi(self):
        self.labelLogin = QLabel("Login", self)
        self.labelLogin.move(180,10)
        self.labelLogin.setFont(QFont("Arial", 20))

        self.labelName = QLabel("Nombre", self)
        self.labelName.move(30,60)

        self.lnedName = QLineEdit(self)
        self.lnedName.move(110,60)
        self.lnedName.resize(220,20)

        self.labelPassword = QLabel("Password", self)
        self.labelPassword.move(30,90)

        self.lnedPassword = QLineEdit(self)
        self.lnedPassword.setEchoMode(QLineEdit.Password)
        self.lnedPassword.move(110,90)
        self.lnedPassword.resize(220,20)

        self.btnLogin = QPushButton("Login", self)
        self.btnLogin.move(100,140)
        self.btnLogin.resize(200,40)

        self.chboxPassword = QCheckBox("Show Password", self)
        self.chboxPassword.move(110,115)
        self.chboxPassword.setChecked(False)

        self.noUser = QLabel("Aun no eres usuario?", self)
        self.noUser.move(90,195)
        self.noUser.setWordWrap(True)
        self.noUser.setFont(QFont("Arial", 7))

        self.btnRegistro = QPushButton("Register", self)
        self.btnRegistro.move(160,195)
        self.btnRegistro.clicked.connect(self.registroUsuario)

        self.chboxPassword.stateChanged.connect(self.showPassword)
        self.btnLogin.clicked.connect(self.clickLogin)

    def clickLogin(self):
        usuarios = {}
        try:
            with open("usuario.txt") as f:
                for line in f:
                    cUsuarios = line.split(" ")
                    usuario = cUsuarios[0]
                    password = cUsuarios[1].rstrip("\n")
                    usuarios[usuario] = password
        except FileNotFoundError:
            f = ("usuario.txt", "w")

        usuario = self.lnedName.text()
        password = self.lnedPassword.text()

        if (usuario, password) in usuarios.items():
            QMessageBox.information(self, "Logeo realizado con Exito", "Logeo realizado con Exito", QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "El nombre de usuario o la contraseña son incorrectos", QMessageBox.Close, QMessageBox.Close)

    def showPassword(self, state):
        if state == Qt.Checked:
            self.lnedPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lnedPassword.setEchoMode(QLineEdit.Password)
    
    def registroUsuario(self):
        self.createNewUser = nuevoUsuario()
        self.createNewUser.show()

    def closeEvent(self, event):
        mensajeCerrar = QMessageBox.question(self, "¿Quieres cerrar la aplicacion?", "¿Estas seguro que desea cerrar la aplicacion?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if mensajeCerrar == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginRes()
    window.show()
    sys.exit(app.exec_())