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
danas = datetime.datetime(2021, 11, 8)
mjesec2 = int(danas.strftime("%m"))

if mjesec2 > mjesec:
    print(name + " " + surname + " ima " + str(dob) + " godinu.")
else:
    print(name + " " + surname + " ima " + str(dob-1) + " godina.")
