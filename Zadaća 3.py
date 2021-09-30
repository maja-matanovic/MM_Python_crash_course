# Zadatak 1
brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []
for element in brojevi:
    x = element % 2
    y = element ** 2
    if x == 1 and y < 49:
        lista.append(y)
    elif x == 1:
        lista.append(element)
print(lista)

# kraj
print("\n ")

# Zadatak 2 (varijanta A)
Pokemon = ["Bulbasaur", "Charmander"]
Category = [10, 100]
list = []

for y in Category:
    for x in Pokemon:
        list.append(x + " " + str(y))

print(list)

# kraj

print("\n ")

# Zadatak 2 (varijanta B)
Pokemon = ["Bulbasaur", "Charmander"]
Category = [10, 100]
list = []
x = 0
y = 0
while y < len(Category):
    while x < len(Pokemon):
        list.append(Pokemon[x] + " " + str(Category[y]))
        x = x + 1
    y = y + 1
    x = 0
print(list)

# kraj

print("\n ")

# Zadatak 3

zaposlenik_267 = {
 "name": "Peter",
 "age": 46,
 "salary": 24098,
 "city": "Washington"
}
zaposlenik_8765 = {
 "name": "Adam",
 "age": 52,
 "salary": 19894,
 "city": "Colorado"
}

zaposlenik_267["name"] = "Perv"
zaposlenik_267["salary"] = 550

zaposlenik_8765["name"] = "Saad Maan"
zaposlenik_8765["salary"] = 550

del zaposlenik_8765["city"], zaposlenik_267["city"]

print(zaposlenik_267)
print(zaposlenik_8765)

copy_267 = zaposlenik_267.copy()
zaposlenik_267.update(zaposlenik_8765)
zaposlenik_8765.update(copy_267)

print("Zaposlenik 267:")
print(zaposlenik_267)
print("Zaposlenik 8765:")
print(zaposlenik_8765)