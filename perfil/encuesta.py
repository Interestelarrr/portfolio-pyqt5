from PyQt5.QtWidgets import QCheckBox, QLabel, QApplication, QWidget
from PyQt5.QtCore import Qt
import sys

class EncuestaApp(QWidget):
    def __init__(self):
        super(EncuestaApp, self).__init__()
        self.inicioUi()

    def inicioUi(self):
        self.setGeometry(100,100,250,200)
        self.setWindowTitle("Encuesta Ventana")
        self.mostrarWidget()

    def mostrarWidget(self):
        label = QLabel("¿Que tipo de persona eres?", self)
        label.resize(250,60)
        label.setAlignment(Qt.AlignCenter)

        regular = QCheckBox("Regular", self)
        regular.move(20,80)
        scriptKiddle = QCheckBox("Script Kiddle", self)
        scriptKiddle.move(20,100)
        hackerProgramador = QCheckBox("Hacker y/o Programador", self)
        hackerProgramador.move(20,120)

        regular.stateChanged.connect(self.imprimirSeleccion)
        scriptKiddle.stateChanged.connect(self.imprimirSeleccion)
        hackerProgramador.stateChanged.connect(self.imprimirSeleccion)

    def imprimirSeleccion(self, status):
        sender = self.sender()
        if status == Qt.Checked:
            print(f"La Opcion {sender.text()} fue elegida")
        else:
            print(f"La Opcion {sender.text()} ya no se eligio")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EncuestaApp()
    window.show()
    sys.exit(app.exec_())

