import random

def get_quant():
    verify = True

    while verify:
        quant = input("Quantidade de jogos: ")
        if not (quant.isdigit()):
            print("Tem que ser número burro. ")
        else:
            verify = False
    return int(quant)

def get_result():
    verify = True

    while verify:
        result = input("Resultado dos jogos: ")
        if result == '':
            print("Resultado não pode ser vazio. ")
        else:
            verify = False
    return result.split()

def generate_line():
    listTemp = []
    for j in range(6):
        verify = True
        while verify:
            num = random.randint(1, 60)
            if num not in listTemp:
                verify = False

        listTemp.append(str(num))

    listTemp.sort()
    return listTemp

def generate_games(quant, games):
    for i in range(quant):
        line = generate_line()
        print(f"Game {i + 1}:", line)
        games.append(line)

def verify_result(games, result):
    print("")
    for game in games:
        count = 0
        gameList = game
        resultList = result

        for x in gameList:
            if x in resultList:
                count += 1

        print(f"{game} : {count} -> {"ganhadora" if count > 3 else "perdedora"}")

def generate_dicionario():
    count = {}
    for i in range(61):
        count[str(i)] = 0

    return count

def count(dicio, games):
    for game in games:
        for numero in game:
            dicio[numero] += 1

def show_dicionary(dicio):
    for i in dicio.keys():
        if dicio[i] != 0:
            print(f"Número: {i} - Quantidade: {dicio[i]}")

if __name__ == "__main__":
    games = []
    dicio = {}
    quant = get_quant()
    print("")
    generate_games(quant, games)
    print("")
    dicio = generate_dicionario()
    count(dicio, games)
    show_dicionary(dicio)