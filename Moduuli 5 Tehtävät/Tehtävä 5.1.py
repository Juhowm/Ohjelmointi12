import random
kuutiot = []
määrä = int(input("Kuinka monta kertaa heitän noppaa? "))
while määrä > 0:
    kuutiot.append(random.randint(1, 6))
    määrä -= 1
for num in kuutiot:
    print(f"Silmäluku oli {num}.")