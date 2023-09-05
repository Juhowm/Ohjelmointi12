luvut = []
luku = input("Anna luku ")
while luku != "":
    int(luku)
    luvut.append(luku)
    luku = input("Anna luku tai paina enteriä lopettaaksesi ")
luvut.sort(reverse=True)
print("Antamistasi luvuista viisi suurinta ovat")
print(luvut[0:5])
