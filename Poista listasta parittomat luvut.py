def poista_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)