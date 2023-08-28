koko = float(input("Mikä on kuhan pituus senttimetreinä? "))
if koko >=37:
    print("Nam!")
else:
    print(f"Liian pieni, laske takaisin järveen! \nKuhan pitäisi olla {37-koko:.0f} senttiä suurempi!")