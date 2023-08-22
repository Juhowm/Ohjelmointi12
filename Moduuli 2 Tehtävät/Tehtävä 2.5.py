leivis_kirj = input("Leiviskömassa: ")
leivis = float(leivis_kirj)
naula_kirj = input("Naulamassa: ")
naula = float(naula_kirj)
luoti_kirj = input("Luotimassa: ")
luoti = float(luoti_kirj)

#1 luoti on 13.3 g
luotimassa = luoti*13.3
#1 naula on 32 luotia
naulamassa = naula*13.3*32
#1 leiviskä on 20 naulaa
leivismassa = leivis*13.3*32*20
tosimassa = luotimassa+naulamassa+leivismassa
tosimassakilo = tosimassa//1000

print(f"Massa modernisti on \n{tosimassakilo:.0f} kilogrammaa")
print(f"ja {tosimassa-tosimassakilo*1000:.2f} grammaa")
