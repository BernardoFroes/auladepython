import sys
import requests 

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QStatusBar)

class Cadastro_cep(QMainWindow):
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
        
        self.cep_input = QLineEdit()
        self.form_layout.addRow("CEP: ", self.cep_input)
        
        self.buscar_cep_button = QPushButton("Buscar Cep")
        #self.layout.addWidget(self.buscar_cep_button)
        self.buscar_cep_button.clicked.connect(self.buscar_cep)
        self.form_layout.addRow(self.buscar_cep_button)
        
        self.rua_input = QLineEdit()
        self.form_layout.addRow("Rua: ", self.rua_input)
        
        self.numero_input = QLineEdit()
        self.form_layout.addRow("Número: ", self.numero_input)
        
        self.bairro_input = QLineEdit()
        self.form_layout.addRow("Bairro: ", self.bairro_input)
        
        self.cidade_input = QLineEdit()
        self.form_layout.addRow("Cidade: ",self.cidade_input)
        
        self.estado_input = QLineEdit()
        self.form_layout.addRow("Estado: ", self.estado_input)
        
        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.clicked.connect(self.cadastrar)
        self.layout.addWidget(self.cadastrar_button)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
    def buscar_cep(self):
        cep = self.cep_input.text()
        if len(cep) == 8 and cep.isdigit():
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if response.status_code == 200:
                data = response.json()
                if "erro" not in data:
                    self.rua_input.setText(data.get("logradouro", ""))
                    self.bairro_input.setText(data.get("bairro", ""))
                    self.cidade_input.setText(data.get("localidade", ""))
                    self.estado_input.setText(data.get("uf",""))
                else:
                    self.status_bar.showMessage("CEP não encontrado", 5000)
            else:
                self.status_bar.showMessage("Erro ao buscar CEP", 5000)
        else:
            self.status_bar.showMessage("CEP Inválido", 5000)
            
    def cadastrar (self):
        nome = self.nome_input.text()
        cep = self.cep_input.text()
        rua = self.rua_input.text()
        numero = self.numero_input.text()
        bairro = self.bairro_input.text()
        cidade = self.cidade_input.text()
        estado = self.estado_input.text()
        if nome and cep and rua and numero and bairro and cidade and estado:
            print(nome)
            self.status_bar.showMessage("Cadastro realizado com sucesso!!!", 5000)
        else:
            self.status_bar.showMessage("Preencha todos os campos", 5000)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cadastro_cep()
    window.show()
    sys.exit(app.exec())