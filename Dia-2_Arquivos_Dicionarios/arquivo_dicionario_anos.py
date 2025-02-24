with open('/home/aluno/Downloads/megasena.txt') as arquivo:
    dados = arquivo.read().split('\n')

ano_fixo = 0

for dado in dados:
    ano = dado[12:16]
    if ano_fixo == 0:
        ano_fixo = ano
        caminho = f"/home/aluno/Downloads/{ano}.txt"
    elif ano_fixo != ano:
        caminho = f"/home/aluno/Downloads/{ano}.txt"
        ano_fixo = ano

    with open(caminho, 'a') as arquivo2:
        dados = arquivo2.write(dado[17:] + "\n")