with open('/home/aluno/Downloads/megasena.txt') as arquivo:
    dados = arquivo.read().split('\n')

pares = []
for dado in dados:
    numeros = dado[17:].split()
    temp = []
    for numero in numeros:
        if int(numero) % 2 == 0:
            temp.append(int(numero))
    if len(temp) == 6:
        pares.append(dado[17:])

# numeros = [int(x) for x in dado[17:].split()]
# temp = [num for num in dezenas if num % 2 == 0]

print(*pares, sep='\n')

with open('/home/aluno/Downloads/pares.txt', 'a') as arquivo:
    dados = arquivo.write("\n".join(pares))