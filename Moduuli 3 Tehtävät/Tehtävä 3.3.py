sp = input("Oletko biologisesti mies vai nainen? ")
if sp != "mies" and sp != "nainen":
    exit("kirjoitusvirhe tai odottamaton arvo sukupuolessa")
hg = float(input("Mikä on hemoglobiiniarvosi yksikkönä g/l? "))
if sp == "mies" and hg > 195 or sp == "nainen" and hg > 175:
    print("Hemoglobiiniarvosi on korkea.")
elif sp == "mies" and hg < 134 or sp == "nainen" and hg < 117:
    print("Hemoglobiiniarvosi on alhainen.")
else:
    print("Hemoglobiiniarvosi on normaali.")
