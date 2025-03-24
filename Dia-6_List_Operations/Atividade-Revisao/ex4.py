"""
4 - Dado um arquivo vendas.csv no seguinte formato: produto, quantidade, preco_unitario
        Mouse,3,50
        Teclado,2,100
        Mouse,1,50

    Crie uma função que:
        • Leia o arquivo.
        • Calcule o total vendido por produto.
        • Retorne um dicionário com o nome do produto e o valor total das vendas.
"""

def total_vendas(nome_arquivo):
    with open(nome_arquivo, "r") as arq:
        dados = arq.read().split("\n")

    dados = [dado.split(",") for dado in dados]

    dicio = {}

    for dado in dados:
        total = int(dado[1]) * int(dado[2])
        if dado[0] in dicio.keys():
            dicio[dado[0]] += total
        else:
            dicio[dado[0]] = total

    return dicio