num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def maior_num(num1,num2):
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("Números iguais")

maior_num(num1,num2)