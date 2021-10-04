import random


def generator(a, b):
    random_lista = []
    for i in range (0,5):
        n = random.randint(a, b)
        random_lista.append(n)

    return random_lista

def usporedba(x, y):
    while True:
        lotto_1 = generator(1, 20)
        lotto_2 = generator(1, 20)
        lotto_1.sort()
        lotto_2.sort()

        if lotto_1 == lotto_2:
            print("Brojevi generirani funkcijom 1: " + str(lotto_1[0]) + ", " + str(lotto_1[1]) + ", " + str(lotto_1[2]) + ", " + str(lotto_1[3]) + ", " + str(lotto_1[4]))
            print("Brojevi generirani funkcijom 2: " + str(lotto_2[0]) + ", " + str(lotto_2[1]) + ", " + str( lotto_2[2]) + ", " + str(lotto_2[3]) + ", " + str(lotto_2[4]))
            print("Čestitam, osvojili ste loto!")
            break
    return lotto_1, lotto_2


lutrija =usporedba(generator(1, 20), generator(1, 20))
