novcanik = "540 hrk"
novcanik = int(novcanik[:3])
iznos_kazne = input("Unesite iznos kazne: ")
valuta = str()

if iznos_kazne.isdigit():
    valuta = input("hrk/eur? ")
else:
    valuta = iznos_kazne.split()[-1]
    valuta = valuta[-3]

if valuta == "e":
    print("Unesena valuta je eur")
    iznos_kazne = iznos_kazne.split()[0]
    iznos_kazne = iznos_kazne.strip("eur")
    iznos_kazne = iznos_kazne.strip(" ")
print(iznos_kazne)