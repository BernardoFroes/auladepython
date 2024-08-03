import sys
import requests 

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit)

class cadastro_cep(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca de CEP")
        self.setMinimumWidth(300)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        
        self.nome_input = QLineEdit()
        self.form_layout.addRow("Nome: ",self.nome_input)
        
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = cadastro_cep()
    window.show()
    sys.exit(app.exec())

