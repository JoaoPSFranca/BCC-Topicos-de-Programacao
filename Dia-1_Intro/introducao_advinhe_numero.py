import random
from multiprocessing.connection import answer_challenge

from unicodedata import digit

num = random.randint(1, 100)
count = 0
answer = False

while count < 7 and not answer:
    verify = True

    while verify:
        userTry = input("Adivinha o número: ")
        if not (userTry.isdigit()):
            print("Eu disse número burro. ")
        else:
            verify = False

    userTry = int(userTry)

    if userTry > num:
        print("É menor o número. ")
        count += 1
    elif userTry < num:
        print("É maior o número. ")
        count += 1
    elif userTry == num:
        print("Não é que você pensa as vezes? ")
        answer = True

if not answer:
    print("Acabaram as chances, cê é burro de mais pra isso. ")