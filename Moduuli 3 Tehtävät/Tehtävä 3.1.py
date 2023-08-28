koko = float(input("Mikä on kuhan pituus senttimetreinä? "))
if koko >= 37:
    print("Mukavan kokoinen kala!")
else:
    print("Liian pieni, laske takaisin järveen! "
          f"\nKuhan pitäisi olla noin {37-koko:.0f} senttiä pidempi!")
