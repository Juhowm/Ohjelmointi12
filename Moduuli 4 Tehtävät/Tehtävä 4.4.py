import random
arvaus = int(input("Arvaa luku välillä 1-10: "))
luku = random.randint(1,10)
while luku < arvaus:
    print("Liian suuri arvaus")
    arvaus = int(input("Arvaa luku välillä 1-10: "))
while luku > arvaus:
    print("Liian pieni arvaus")
    arvaus = int(input("Arvaa luku välillä 1-10: "))
if luku == arvaus:
    print("Oikein")
