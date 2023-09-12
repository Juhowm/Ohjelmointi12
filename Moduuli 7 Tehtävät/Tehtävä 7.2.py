nimet = set()
lisäys = input("Anna nimi: ")
uusi = True
while lisäys != "":
    for n in nimet:
        if n != lisäys:
            uusi = True
            #katsoo kaikki läpi
        else:
            uusi = False
            break
            #loppuu heti kun löytyy sama
    if uusi is True:
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")
    nimet.add(lisäys)
    lisäys = input("Anna nimi tai paina enteriä lopettaaksesi: ")
for n in nimet:
    print(n)
