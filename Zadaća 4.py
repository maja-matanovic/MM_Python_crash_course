novcanik = "540 hrk"
novcanik = int(novcanik[:3])
iznos_kazne = input("Unesite iznos kazne: ")
valuta = str()

if iznos_kazne.isdigit():
    valuta = input("hrk/eur? ")
else:
    valuta = iznos_kazne.split()[-1]

if valuta == "eur":
    print("Unesena valuta je eur")
    iznos_kazne = iznos_kazne.split()[0]
    iznos_kazne = int(iznos_kazne)
    iznos_kazne = iznos_kazne * 7.65
    print("Iznos u kunama je " + str(iznos_kazne) + " hrk.")
else:
    iznos_kazne = iznos_kazne.split()[0]
    iznos_kazne = iznos_kazne.strip()
    iznos_kazne = int(iznos_kazne)


if iznos_kazne < novcanik:
    print("Ajme, mogao sam popiti jos jedan gemist.")
elif iznos_kazne >= novcanik and iznos_kazne <= 1000:
    print("Nije tak ni strasno.")
elif iznos_kazne > 1000:
    print("Hoces ti reci mojoj zeni?")