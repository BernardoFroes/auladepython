class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
pessoa1 = Pessoa("Érico", 36)

print(pessoa1.nome)