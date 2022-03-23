# zadatak 1
sentence = "yzf xrl prltty gzzd xt thms"
correct_sentence = sentence.replace("x", "a").\
    replace("l", "e").replace("m", "i").replace("z", "o").replace("f", "u")
print(correct_sentence)

# zadatak 2
sentence_2 = "Inoslav je danas slistio cijeli avokado."

print(sentence_2[1] + sentence_2[5] + sentence_2[8]
      + sentence_2[10] + sentence_2[15] + sentence_2[19])

# zadatak 3
sentence_3 = "StvarnoSPACEsuSPACEgrozneSPACEoveSPACEMacbookSPACEProSPACEtipkovnice."
print(sentence_3.replace("SPACE", "\n"))

# zadatak 4
sentence_4 = "jasamigormancesvirambubnjeveivolimte"
# TODO: Vjerujem da znas to, ali mogla si ovo jednostavnije napraviti - sentence_4[-7:].
#  Lijepo sto si htjela i razmak dodati :)
print(sentence_4[29:34] + " " + sentence_4[34:])

# zadatak 5
sentence_5 = "Ajde kupi Cokolino, gladan sam!"
sentence_6 = "Nalazimo se sutra u 7 kod Lane. Stizes?!?"
sentence_7 = "Pao sam s romobila. Please zovi hitnu."
print(float((len(sentence_5) + len(sentence_6) + len(sentence_7))/3))

# zadatak 6
sentence_8 = ">w<<>o[[[[[w{}{i::a&*!%m@@@re(a&%$l;:;l__—y?*aLKJm*a**z!e$$dSDaMBMMt%t*?=h222iQWEs%$ASD&p&o%i123n!—t"

for x in sentence_8:
    if x.isalpha() and x.islower():
        print(x, end="")
print("")

# zadatak 7
sentence_9 = "ptof xn yn rnhf mfpjwnhf"
for x in sentence_9:
    print(chr(ord(x) - 5), end="")
