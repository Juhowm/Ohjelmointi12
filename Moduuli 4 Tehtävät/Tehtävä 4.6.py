import random
pistesis = 0
#ympyrän siälle päätyvien pisteiden määrä
pistelrg = 0
#ympyrän ulkopuolelle päätyvien pisteiden määrä
pistemr = int(input("Anna arvottavien pisteiden määrä"))
#satunnaisten pisteiden määrä
if pistemr < 0:
    exit("negatiiviset luvut eivät kelpaa")
while pistemr != 0:
    x = random.randrange(-1, 1)
    y = random.randrange(-1, 1)
    if x**2+y**2 < 1:
        pistesis += 1
    pistemr -= 1
    pistelrg += 1
print(f"{4*pistesis/pistelrg}")
