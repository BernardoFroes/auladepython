import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,QPushButton,QWidget)

app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
window.setWindowTitle("Menu Principal")
window.setMinimumWidth(400)
window.setMinimumHeight(400)

botao = QPushButton("Clique em mim")
botao.setStyleSheet("font-size: 40px; color: blue; background-color: white")


botao1 = QPushButton("Clique em mim")
botao1.setStyleSheet("font-size: 40px; color: white; background-color: red")

botao2 = QPushButton("Clique em mim")
botao2.setStyleSheet("font-size: 40px; color: white; background-color: purple")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1,1,1,1)
layout.addWidget(botao1, 1,2,1,1)
layout.addWidget(botao2, 2,1,1,2)

def slot_example(status_bar):
    status_bar.showMessage("Em Execução")
    
status_bar = window.statusBar()
status_bar.showMessage("Barra de Status")

menu = window.menuBar()
menu1 = menu.addMenu("Primeiro Menu")
acao1 = menu1.addAction("Ação de Execução")
acao2 = menu1.addAction("Ação 2")

acao1.triggered.connect(lambda: slot_example(status_bar))

menu2 = menu.addMenu("Segundo Menu")
acao1 = menu2.addAction("Ação 3")
acao2 = menu2.addAction("Ação 4")

window.show()

app.exec()