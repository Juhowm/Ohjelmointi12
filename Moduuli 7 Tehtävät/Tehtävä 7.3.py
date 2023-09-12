asemat = {"EFHK": "Helsinki-Vantaan lentokenttä", }
hyv = ("lisää", "hae", "stop")
#hyväksytyt hakutermit


def terv():
    terveh = input("Jos haluat lisätä tietokantaan lentokentän, kirjoita 'lisää'"
                    "\nJos haluat etsiä lentokenttää ICAO-koodilla, kirjoita 'hae'"
                    "\nJos haluat lopettaa ohjelman, kirjoita 'stop'"
                    "\nNäistä poikkeavia ei hyväksytä ")
    return terveh


def lisäys(icao, asema):
    lisä = asemat[icao] = asema
    return lisä


def haku(hicao):
    if hicao in asemat:
        print(f"{asemat[hicao]}")
    else:
        print("Asemaa ei löytynyt tietokannastamme")


terve = terv()
for s in hyv:
    if terve != s:
        print("Tunnistamaton input")
        terve = terv()
        #tarkistaa onko kirjoitettu hakutermi hyväksyttyjen listalla ja pyytää uuden jos ei
while terve == "lisää":
    lisää = lisäys(input("Anna aseman ICAO: "), input("Anna asenan nimi: "))
    terve = terv()
while terve == "hae":
    haku(input("Anna etsimäsi aseman ICAO: "))
    terve = terv()
while terve == "stop":
    exit("Hyvästi")
