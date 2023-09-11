def muunto(gallonat):
    litrat = gallonat*3.785
    return litrat


määrä = int(input("Anna nesteen määrä gallonoina: "))
loppu = muunto(määrä)
while määrä >= 0:
    print(f"{määrä} gallonaa on {loppu} litraa"
          f"\njos haluat lopettaa ohjelman, syötä negatiivinen luku."
          f"\nMuuten syötä positiivinen luku")
    määrä = int(input("Anna nesteen määrä gallonoina: "))
    muunto(määrä)
    loppu = muunto(määrä)
else:
    exit("Moi moi")
