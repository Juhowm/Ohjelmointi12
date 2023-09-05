luku = int(input("Anna kokonaisluku: "))
onalk = True
for num in range(2, luku):
    if luku % num == 0 and onalk:
        onalk = False
        print("Antamasi luku ei ole alkuluku")
if onalk:
    print("Antamasi luku on alkuluku")
