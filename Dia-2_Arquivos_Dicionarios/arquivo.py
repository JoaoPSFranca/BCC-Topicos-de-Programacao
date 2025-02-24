with open('/home/aluno/Downloads/megasena.txt') as arquivo:
    dados = arquivo.read().split('\n')

dicionario = {}
for x in dados:
    y = x[17:].split()
    y = sum(int(i) for i in y)
    if y in dicionario.keys():
        dicionario[y] += 1
    else:
        dicionario[y] = 1

dicionario_ordenado = dict(sorted(dicionario.items(), key = lambda item: item[1], reverse=True))

for x,y in dicionario_ordenado.items():
    print(x, y)