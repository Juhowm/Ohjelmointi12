import random


def heitto():
    luku = random.randint(1, 6)
    return luku


noppa = heitto()
while noppa != 6:
    print(f"{noppa}\nnoppaa heitetään uudestaan")
    heitto()
    noppa = heitto()
else:
    print(f"{noppa}\nsait kutosen!")
