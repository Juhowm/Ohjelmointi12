def poisto(luklis):
    luklis = luklis.copy()
    for n in luklis:
        if n % 2 != 0:
            luklis.remove(n)
    lista = luklis
    return lista


luli = [1, 2, 3, 4, 5, 6]
pois = poisto(luli)
print(luli)
print(pois)
