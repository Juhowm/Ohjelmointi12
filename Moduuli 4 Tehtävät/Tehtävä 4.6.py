import math
import random

pistemr = int(input("Anna arvottavien pisteiden määrä"))
if pistemr <= 0:
    exit("negatiiviset luvut eivät kelpaa")
while pistemr != 0:
    x = random.randrange(-1, 1)
    y = random.randrange(-1, 1)
    pistemr -= 1
