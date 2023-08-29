import random
pistesis = 0
pistelrg = 0
pistemr = int(input("Anna arvottavien pisteiden määrä"))
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
