tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1+tupla2

print(tupla3)
lista1 = []
for i in range (0,3):
    lista1.append(tupla1[i]+tupla2[i])
print(lista1)
    