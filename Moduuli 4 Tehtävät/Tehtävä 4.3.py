luvut = []
luku = input("anna luku: ")
while luku != "":
    luku = float(luku)
    luvut.append(luku)
    luku = input("anna luku: ")
print(f"Pieni luku antamistasi oli {min(luvut)}"
      f"\nja suurin oli {max(luvut)}")
