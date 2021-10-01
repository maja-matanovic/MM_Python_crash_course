import random
unos = str(input("Unesite 5 brojeva od 2 do 20 "))
unos = unos.split(" ")
unesena_lista = []
for x in unos:
    unesena_lista.append(int(x))
print("Uneseni brojevi su: ")
print(str(unesena_lista[0]) + ", " + str(unesena_lista[1]) + ", " + str(unesena_lista[2]) + ", " + str(unesena_lista[3]) + ", "+ str(unesena_lista[4]))


def generator(a,b):
    random_lista = []

    for i in range (0,5):
        n = random.randint(a, b)
        random_lista.append(n)

    return random_lista


def usporedba(list1, list2):
    print("Brojevi izvučeni u ovom kolu su ")
    while True:
        lotto = generator(1, 20)
        lotto.sort()
        unesena_lista.sort()

        if lotto == unesena_lista:
            print(str(lotto[0]) + ", " + str(lotto[1]) + ", " + str(lotto[2]) + ", " + str(lotto[3]) + ", "+ str(lotto[4]))
            print("Čestitam, osvojili ste lotto")
            break


    return lotto


lutrija = usporedba(generator(1, 20), unesena_lista)


















