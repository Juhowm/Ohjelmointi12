def summaus(luklis):
    summa = 0
    for luku in luklis:
        summa = summa + luku
    return summa


luli = [1, 2, 3, 4, 5]
lasku = summaus(luli)
print(lasku)
