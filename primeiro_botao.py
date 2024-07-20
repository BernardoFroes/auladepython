import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton("Clique em mim")
botao.setStyleSheet("font-size: 40px; color: blue; background-color: white")
botao.show()

botao1 = QPushButton("Clique em mim")
botao1.setStyleSheet("font-size: 40px; color: white; background-color: red")
botao1.show()

app.exec()