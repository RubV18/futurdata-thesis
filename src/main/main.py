from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

class ProcessWizardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        uic.loadUi('ui/main.ui', self)






if __name__ == '__main__':
    app = QApplication([])
    window = ProcessWizardWindow()
    window.show()
    app.exec()