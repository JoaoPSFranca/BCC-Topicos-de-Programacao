"""
2 - (1,0) Faça um programa que leia um arquivo e armazene em uma lista todas as palavras do
texto, verifique qual das palavras possui a maior quantidade de vogais, esta palavra e todas
as outras com a mesma quantidade devem ser impressas na tela numeradas de 1 a n,
conforme exemplo:
    Palavras com 6 vogais:
    Abacateria
    Jurubebeira
"""

def conta_vogal(palavra):
    count = 0

    for i in palavra:
        if i in ("a", "e", "i", "o", "u"):
            count += 1

    return count

def quantidade_vogais(nome_arquivo):
    with open(nome_arquivo) as arq:
        dados = arq.read().split("\n")

    dicio = {}

    for dado in dados:
        for palavra in dado.split(" "):
            if palavra not in dicio.keys():
                dicio[palavra] = conta_vogal(palavra)

    dicio = dict(sorted(dicio.items(), key=lambda x: x[1], reverse=True))

    max = dicio[0][1]

    print(f"Palavras com {max} vogais: ")
    for x, y in dicio.items():
        if y != max:
            break

        print(x)