import random


def heitto(sivut):
    luku = random.randint(1, sivut)
    return luku


maks = int(input("Anna nopan suurin silmäluku: "))
satu = heitto(maks)
while satu != maks:
    print(f"{satu}\nnoppaa heitetään uudestaan")
    heitto(maks)
    satu = heitto(maks)
else:
    print(f"{satu}\nsait korkeimman arvon!")
