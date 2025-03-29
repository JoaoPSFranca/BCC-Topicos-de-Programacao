"""
1 - (1,0) Faça um programa que leia um arquivo texto qualquer e gere um segundo arquivo
conforme o modelo abaixo. As linhas devem ser numeradas, mostre a maior e a menor
palavra do texto. Mostre também em um dicionário somente as palavras repetidas no texto
e a quantidade de vezes que elas aparecem. Faça um resumo da quantidade de letras por
tamanho da palavra.

    0001 aaaa aaaaa aaaa xxxxx vvvvvvvvvvvv aaaaa
    0002 ccccccc ccccccc cc ccccc cccccc
    0003 vvvv vvvvv vvvvv

    Maior palavra: vvvvvvvvvvvv Menor palavra: cc
    Palavras repetidas:
    Repetidas

    aaaa => 2
    aaaaa => 2
    vvvvv => 2

    Resumo
    Com 2 letras = 2
    Com 3 letras = 4
    Com 5 letras = xxx
"""

def gerar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arq:
        dados = arq.read().split("\n")

    with open(nome_arquivo + "_v2", "w") as arq2:
        i = 0

        dicio = {}
        quantidade_letras = {}
        maior_palavra = ""
        menor_palavra = ""
        texto = ""

        for dado in dados:
            texto += f"{i:04d} " + dado + "\n"
            i += 1

            for palavra in dado.split(" "):
                if palavra in dicio.keys():
                    dicio[palavra] += 1
                else:
                    dicio[palavra] = 1

                if len(palavra) in quantidade_letras.keys():
                    quantidade_letras[len(palavra)] += 1
                else:
                    quantidade_letras[len(palavra)] = 1

                if len(palavra) > len(maior_palavra):
                    maior_palavra = palavra

                if len(menor_palavra) > len(palavra) or menor_palavra == "":
                    menor_palavra = palavra

        dicio = dict(sorted(dicio.items(), key=lambda item: item[1], reverse=True))
        quantidade_letras = dict(sorted(quantidade_letras.items(), key=lambda item: item[0], reverse=True))
        texto += f"\nMaior Palavra: {maior_palavra} Menor Palavra: {menor_palavra}\n"
        texto += f"Palavras repetidas: \nRepetidas \n"

        for x, y in dicio.items():
            texto += f"\n{x} => {y}"

        texto += f"\n\nResumo"
        for x, y in quantidade_letras.items():
            texto += f"\nCom {x} letras = {y}"

        arq2.write(texto)
