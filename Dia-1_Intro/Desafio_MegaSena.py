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
    return result

def generate_line():
    listTemp = []
    for j in range(6):
        verify = True
        while verify:
            num = random.randint(1, 60)
            if num not in listTemp:
                verify = False

        listTemp.append(num)

    listTemp.sort()
    line = [str(x + 100)[1:] for x in listTemp]
    return " ".join(line)

def generate_games(quant, games):
    for i in range(quant):
        line = generate_line()
        print(f"Game {i + 1}:", line)
        games.append(line)

def verify_result(games, result):
    print("")
    for game in games:
        count = 0
        gameList = game.split()
        resultList = result.split()

        for x in gameList:
            if x in resultList:
                count += 1

        print(f"{game} : {count} -> {"ganhadora" if count > 3 else "perdedora"}")

if __name__ == "__main__":
    games = []
    quant = get_quant()
    print("")
    generate_games(quant, games)
    print("")
    verify_result(games, get_result())
