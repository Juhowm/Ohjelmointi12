kt = "python"
ss = "rules"
arvkt = input("anna käyttäjätunnus: ")
arvss = input("anna salasana ")
arvmr = 0
while arvkt != kt or arvss != ss:
    print("väärä salasana tai käyttäjätunnus")
    arvmr = arvmr + 1
    arvkt = input("anna käyttäjätunnus: ")
    arvss = input("anna salasana: ")
    if arvmr >= 4:
        break
if arvkt == kt and arvss == ss:
    print("Tervetuloa")
else:
    exit("Pääsy kielletty")
