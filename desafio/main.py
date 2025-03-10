import numpy

def pegar_3():
    with open('ALEATORIO.TXT') as arquivo:
        dados = arquivo.read().split('\n')
        arquivo.close()

    dicionario = {}
    for x in dados:
        y = x.split()
        for i in y:
            if i in dicionario.keys():
                dicionario[i] += 1
            else:
                dicionario[i] = 1

    dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=False))
    list = []
    count = 0
    for x, y in dicionario_ordenado.items():
        list.append(x)
        count += 1
        if count == 3:
            break
    return list, dados

def pegar_linha_coluna(num, dados):
    count = 0
    i = 0
    j = 0
    for x in dados:
        count += 1
        y = x.split()
        if num in y:
            i = count
            j = y.index(num) + 1

    if j < 10:
        j = "0" + str(j)
    else:
        str(j)

    return str(i) + j

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_prime3(number):
    sieve = numpy.ones(number + 1, dtype=bool)
    sieve[:2] = False
    for num in range(2, int(number ** 0.5) + 1):
        if sieve[num]:
            sieve[num * num::num] = False
    return numpy.nonzero(sieve)[0]

def separar_colunas(dados):
    list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for x in dados:
        listTemp = x.split()
        for i in range(len(listTemp)):
            list[i].append(int(listTemp[i]))

    return list

def find_col(lista):
    max = 0
    col_primos = []

    for i in lista:
        count = 0
        col_temp = []

        for j in i:
            if is_prime(j):
                count += 1
                col_temp.append(j)

        if count > max:
            max = count
            col_primos = col_temp

    return col_primos

if __name__ == "__main__":
    list, dados = pegar_3()

    senha1 = pegar_linha_coluna(list[1], dados)
    print(f"Primeira Senha: {senha1}")
    list_primos = is_prime3(100)
    list_colunas = separar_colunas(dados)
    coluna = find_col(list_colunas)

    print(sum(coluna))