numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
lista = []

for x in numbers:
    if x % 2 == 1:
        lista.append(x)

suma = sum(lista)
print(suma)
