from datetime import datetime
class Pessoa: 
    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc
        
    def calcular_idade (self):
        hoje = datetime.now()
        if (self.data_nasc.month < hoje.month or self.data_nasc.month == hoje.month and self.data_nasc.day <= hoje.day):
            idade = hoje.year-self.data_nasc.year
        else:
            idade = hoje.year-self.data_nasc.year-1
        return idade
class Pet:
    def __init__(self,nome, idade, cor, raça,tutor):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        self.cor = cor
        self.tutor = tutor
    def som (self):
        pass
        
class Cachorro(Pet):
    def __init__(self, nome, raça, cor, idade,tutor):
        super().__init__(nome,idade,raça,cor,tutor)
        
    def som(self):
        return "auuuuuu"

class Gato(Pet):
    def __init__(self, nome, raça, cor, idade,tutor):
        super().__init__(nome,idade,raça,cor,tutor)
        
    def som(self):
        return "miau"
    
pessoa1 = Pessoa("Érico", datetime(1987,9,16))
cachorro1 = Cachorro("Mel","poodle","branca",3,pessoa1)
print(pessoa1.calcular_idade)

