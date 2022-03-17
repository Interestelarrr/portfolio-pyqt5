from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
import sys

class eventoCerrar(QWidget):
    def __init__(self):
        super(eventoCerrar, self).__init__()
    
    def closeEvent(self, event):
        cuadro = QMessageBox.warning(self, "Cerrar", "¿Estas seguro que deseas cerrar la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if cuadro == QMessageBox.Yes:
            event.accept()
        elif cuadro == QMessageBox.No:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = eventoCerrar()
    window.show()
    sys.exit(app.exec_())