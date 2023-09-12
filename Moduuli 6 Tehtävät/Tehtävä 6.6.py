import math


def hintaper(halk, hinta):
    suhde = hinta/(math.pi * ((halk/2)**2))
    return suhde


hinta1 = float(input("Anna ensimmäisen pitsan hinta euroina: "))
koko1 = float(input("Anna ensimmäisen pitsan halkaisija metreinä: "))
loppu1 = hintaper(koko1, hinta1)
print(f"Ensimmäinen pizza maksaisi siis noin {loppu1:.2f} euroa per neliömetri.")

hinta2 = float(input("Anna toisen pitsan hinta euroina: "))
koko2 = float(input("Anna toisen pitsan halkaisija metreinä: "))
loppu2 = hintaper(koko2, hinta2)
print(f"Toinen pizza maksaisi siis noin {loppu2:.2f} euroa per neliömetri.")

if loppu1 > loppu2:
    print("Eli toisesta pitsasta saa paremmin rahasta arvoa.")
elif loppu1 < loppu2:
    print("Eli ensimmäisestä pitsasta saa paremmin rahasta arvoa.")
else:
    print("Eli molemmista pitsoista saa yhtä paljon rahasta arvoa.")
