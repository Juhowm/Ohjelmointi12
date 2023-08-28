vuosi = int(input("Kirjoita jokin vuosiluku: "))
if vuosi % 100 == 0 and vuosi % 400 == 0 or vuosi % 4 == 0 and not vuosi % 100 == 0:
    print("Antamasi vuosi on karkausvuosi.")
else:
    print("Antamasi vuosi ei ole karkausvuosi.")
