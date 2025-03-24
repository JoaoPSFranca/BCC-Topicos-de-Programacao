"""
3 - Crie uma função chamada filtrar_maioridade(pessoas) que recebe uma lista de
dicionários, onde cada dicionário contém nome e idade, e retorna uma lista
apenas com os nomes de quem tem idade maior ou igual a 18.
"""

def filtrar_maioridade(pessoas):
    dicio = [{}]

    # dicio = list(filter(lambda x: x["idade"] > 18, pessoas))

    for pessoa in pessoas:
        if pessoa["idade"] >= 18:
            dicio.append(pessoa)

    return dicio