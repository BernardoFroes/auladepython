import sys
from PySide6.QtWidgets import (QApplication, QWidget,QVBoxLayout,QTextEdit,QComboBox,QPushButton,QLabel)
from googletrans import Translator

class GoogleTranslator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tradutor = Translator()
        
        self.idiomas = {
            "  ": "  ",
            "en": "Inglês",
            "es": "Espanhol",
            "fr": "Francês",
            "de": "Alemão",
            "it": "Italiano",
            "pt": "Português"
        }
        
        self.setWindowTitle("Tradutor de Idiomas")
        self.setGeometry(100,100,400,300)
        
        layout = QVBoxLayout()
        
        self.texto_input = QTextEdit(self)
        self.texto_input.setPlaceholderText("Digite o texto a ser traduzido")
        layout.addWidget(self.texto_input)
        
        self.selecao_idioma = QComboBox(self)
        self.selecao_idioma.addItems([f"{nome} ({codigo})" for codigo, nome in self.idiomas.items()])
        layout.addWidget(QLabel("Selecione o Idioma de destino: "))
        layout.addWidget(self.selecao_idioma)
        
        botao_traduzir = QPushButton("Traduzir",self)
        botao_traduzir.clicked.connect(self.traduzir_texto)
        layout.addWidget(botao_traduzir)
        
        self.texto_saida = QTextEdit(self)
        self.texto_saida.setReadOnly(True)
        layout.addWidget(QLabel("Texto Traduzido: "))
        layout.addWidget(self.texto_saida)
        
        self.setLayout(layout)
        
    def traduzir_texto (self):
        texto = self.texto_input.toPlainText()
        
        texto_selecionado = self.selecao_idioma.currentText()
        idioma_destino = [codigo for codigo, nome in self.idiomas.items() if f"{nome} ({codigo})" == texto_selecionado][0]
    
        try:
            traducao = self.tradutor.translate(texto,dest=idioma_destino)
            self.texto_saida.setPlainText(traducao.text)
        except Exception as e:
            self.texto_saida.setPlainText(f"Erro ao traduzir:  {e}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    google_translator = GoogleTranslator()
    google_translator.show()
    sys.exit(app.exec())
    