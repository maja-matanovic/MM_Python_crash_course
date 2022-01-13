pozvani = ["Otto", "Neven", "Mario", "Lana", "Ana", "Tihana", "Ino", "Nikolina"]
lista = []

for x in pozvani:
    x = x.lower()
    if x[::-1] != x:
        lista.append(x)
        lista.sort()

print(lista)
