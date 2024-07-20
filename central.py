import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout,QWidget

app = QApplication(sys.argv)

botao = QPushButton("Clique em mim")
botao.setStyleSheet("font-size: 40px; color: blue; background-color: white")


botao1 = QPushButton("Clique em mim")
botao1.setStyleSheet("font-size: 40px; color: white; background-color: red")

botao2 = QPushButton("Clique em mim")
botao2.setStyleSheet("font-size: 40px; color: white; background-color: purple")

botao3 = QPushButton("Clique em mim")
botao3.setStyleSheet("font-size: 40px; color: blue; background-color: white")

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1,1,1,1)
layout.addWidget(botao1, 1,2,1,1)
layout.addWidget(botao2, 2,1,1,2)
layout.addWidget(botao3, 1,3,2,1)

central_widget.show()

app.exec()