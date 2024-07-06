ano_nasc = [1979,1985,1989,1994,1979,1985,1997,1998,2000,2002]
idades = []
ano_atual = 2024
adicionar_ano_nasc = lambda ano: ano_nasc.append(ano)

for ano in ano_nasc:
    #print(ano)
    idades.append(ano_atual-ano)

for idade in idades:
    print(idade)

print(max(idades))
print(min(idades))
idades.sort(reverse=True)
print(idades)