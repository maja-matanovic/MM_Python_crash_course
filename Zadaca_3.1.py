izjava = input("Unesite svoju izjavu: ")
i = 0

for x in izjava:
    if x.isalpha():
        i += 1

if i < 20 or i > 40:
    print("Niste prošli detektor laži.")
elif 20 <= i <= 40:
    izjava = izjava.split()
    for y in izjava:
        if y == "joj" or y == "hm":
            print("Niste prošli detektor laži.")
            break
        else:
            continue
    else:
        print("Prošli ste detektor laži")
