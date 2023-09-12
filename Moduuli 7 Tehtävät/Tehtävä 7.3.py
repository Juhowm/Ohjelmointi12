asemat = {"EFHK": "Helsinki-Vantaan lentokenttä", }
hyv = ("lisää", "hae", "stop")


def terv():
    tere = input("Jos haluat lisätä tietokantaan lentokentän, kirjoita 'lisää'"
                 "\nJos haluat etsiä lentokenttää ICAO-koodilla, kirjoita 'hae'"
                 "\nJos haluat lopettaa ohjelman, kirjoita 'stop'"
                 "\n")
    return tere


print(hyv)
terve = terv()
for s in hyv:
    if terve != s:
        print("Tunnistamaton input")
        terve = terv()
while terve == "lisää":
    asemat[input("Anna aseman ICAO: ")] = input("Anna asenan nimi: ")
    terve = terv()
while terve == "hae":
    haku = input("Anna etsimäsi aseman ICAO: ")
    if haku in asemat:
        print(f"{asemat[haku]}")
    else:
        print("Asemaa ei löytynyt tietokannastamme")
    terve = terv()
while terve == "stop":
    exit("Hyvästi")
