"""
1 - Crie uma função chamada contar_palavras_arquivo(nome_arquivo) que recebe
o nome de um arquivo .txt, abre-o e retorna um dicionário com as palavras únicas
e suas respectivas quantidades de ocorrência no texto.
"""

def contar_palavra(nome_arquivo):
    dicio = {}

    with open(nome_arquivo, "r") as arq:
        dados = arq.read().replace("\n", " ").split(" ")

    for dado in dados:
        if dado in dicio.keys():
            dicio[dado] += 1
        else:
            dicio[dado] = 1

    return dicio
