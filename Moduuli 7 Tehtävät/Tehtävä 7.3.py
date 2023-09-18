asemat = {"EFHK": "Helsinki-Vantaan lentokenttä",
          "KJFK": "John F. Kennedyn kansainvälinen lentokenttä"}
hyv = {"lisää", "hae", "stop"}


def terv():
    tere = input("Jos haluat lisätä tietokantaan lentokentän, kirjoita 'lisää'"
                 "\nJos haluat etsiä lentokenttää ICAO-koodilla, kirjoita 'hae'"
                 "\nJos haluat lopettaa ohjelman, kirjoita 'stop' ")
    return tere


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
else:
    exit("käynnistä uudelleen")
