def ler_arquivo(arquivo):
    with open(arquivo, "r") as arq:
        dados = arq.read().split("\n")

        lista = []

        for dado in dados:
            dado_strip = dado.replace("  ", " ").split(" ")

            if dado_strip[-1].strip() == "":
                dado_strip.pop()

            id = dado_strip.pop(0)
            valor = dado_strip.pop()
            situacao = dado_strip.pop()
            cpf = dado_strip.pop()
            nome = " ".join(dado_strip)

            dicio_temp = {
                "id":id,
                "nome":nome,
                "cpf":cpf,
                "situacao":situacao,
                "valor":valor
            }

            lista.append(dicio_temp)

    return lista

lista = ler_arquivo("arquivo.txt")
print(lista)