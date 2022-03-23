lista = []


def automehanicar(ime):
    print(ime)
    remen = float(input("Popravak zupčastog remena: ").strip(" kn"))
    branik = float(input("Popravak branika: ").strip(" kn"))
    popust = float(input("Popust: ").strip(" %"))
    # TODO: Nedostaje ti provjera da popust nije veci od 100 i da nije negativna vrijednost.
    #  Boundary value analysis ovo-ono :) Osim toga, odlicno!
    suma = (remen + branik) - (popust / 100) * (remen + branik)
    print("Ukupno: " + str(suma))
    return suma


a = automehanicar("Renato")
lista.append(a)
b = automehanicar("Marino")
lista.append(b)
c = automehanicar("Luka")
lista.append(c)

if min(lista) == a:
    print("Najbolja opcija je Renato: " + str(a) + " kn")
if min(lista) == b:
    print("Najbolja opcija je Marino: " + str(b) + " kn")
if min(lista) == c:
    print("Najbolja opcija je Luka: " + str(c) + " kn")
