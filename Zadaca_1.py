import datetime
# zadatak 2
name = "Maja"
surname = "Matanovic"

print(name.upper() + " " + surname.upper())

# zadatak 3
dan = 15
mjesec = 10
godina = 1990

for x in dan, mjesec, godina:
    print(str(x), end=". ")

print("")

# zadatak 4
dob = 2021 - godina

print(name + " " + surname + " ima " + str(dob) + " godinu.")

# zadatak 5
# TODO: Koristeci datetime module i njegovu date klasu, mozes dohvatiti trenutno vrijeme koristeci metodu today()
danas = datetime.datetime(2021, 11, 8)
mjesec2 = int(danas.strftime("%m"))

# TODO: Ovakvo rjesenje uzima u obzir samo trenutni mjesec, no, trebalo bi i provjeriti trenutni dan :)
#  Recimo, ocekujem razliciti output za datume 14.10.2022. i 16.10.2022
if mjesec2 > mjesec:
    print(name + " " + surname + " ima " + str(dob) + " godinu.")
else:
    print(name + " " + surname + " ima " + str(dob-1) + " godina.")
