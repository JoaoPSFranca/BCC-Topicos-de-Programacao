"""
3 - (1,0) Faça um programa que leia um arquivo texto, armazene as palavras de cada linha numa
lista, para cada linha lida, classifique essa lista em ordem crescente, de acordo com a
quantidade de letras de cada palavra, em seguida mostre as linhas com as palavras
ordenadas pelo tamanho conforme o exemplo:
    ‘|um|dois|cinco|catorze|’
"""

def ler_arquivo(arquivo):
    with open(arquivo) as arq:
        linhas = arq.readlines()

    return [linha.strip() for linha in linhas]

def contar_letras(linhas):
    linhas_ordenadas = []

    for linha in linhas:
        linha = linha.split()
        linha = sorted(linha, key=len)
        linhas_ordenadas.append(linha)

    return linhas_ordenadas

def mostrar_linhas(nome_arquivo):
    linhas = ler_arquivo(nome_arquivo)
    linhas_ordenadas = contar_letras(linhas)

    for linha in linhas_ordenadas:
        linha = "|" + "|".join(linha) + "|"
        print(linha)
