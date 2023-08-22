leivis_kirj = input("Leiviskömassa: ")
leivis = float(leivis_kirj)
naula_kirj = input("Naulamassa: ")
naula = float(naula_kirj)
luoti_kirj = input("Luotimassa: ")
luoti = float(luoti_kirj)

luotimassa = luoti*13.3
naulamassa = naula*13.3*32
leivismassa = leivis*13.3*32*20

print(f"Massa modernisti on siis {(luotimassa+naulamassa+leivismassa):.3f}")