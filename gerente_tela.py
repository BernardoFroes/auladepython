import sys

from teste import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow (QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show
    app.exec()
