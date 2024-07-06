def media_nota(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3
def aprovado():
    media = media_nota(nota1,nota2,nota3)
    if  media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota "))

print(media_nota(nota1,nota2,nota3))
print(aprovado())




