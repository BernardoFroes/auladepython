lista = [1,2,3,4,5,6,7,8,9]
lista2 = [7,8,12,17]
print(lista)
lista.append(10)
print(lista)
lista.insert(5,3)
print(lista)
lista.extend(lista2)
print(lista)
lista.remove(2)
print(lista)
elemento = lista.pop(3)
print(elemento)
print(lista)
del lista[7]
print(lista)
#lista.clear()
#print(lista)
print(lista[1:4])
print(lista[:3])
print(lista[::4])
print(lista.index(3))
lista3 = [1,1,2,2,3]
print(lista3.count(2))
print(3 in lista)
print(0 in lista)