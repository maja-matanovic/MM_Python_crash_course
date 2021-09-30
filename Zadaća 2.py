#Zadatak 1
Ludilo = "?oker ib oK .unohtyP yhtnoM op emi oibod ej nohtyP ,aD"
print(Ludilo[::-1])

#Zadatak 2
slice = "M a kuz im taj sli ce kao da sam ga sam pi sao /la ."
print(slice[:1] + slice[2:7] + slice[8:18] + slice[19:42] + slice[43:46] + slice[47:])

#Zadatak 3
print("\n \n")
ime_knjige = input("Unesite ime knjige ")
ime_autora = input("Unesite ime autora ")
if len(ime_knjige) > 30 and ime_autora != "Hemingway":
    print("Ma jel' moguće?")
elif len(ime_knjige) > 30 and ime_autora == "Hemingway":
    print("Ok, tako već može")
elif len(ime_knjige) == 25 and ime_autora == "":
    print("Šta, nismo bili u školi?")
elif ime_knjige[0:2] == "In":
    print("Skoro Infinum")