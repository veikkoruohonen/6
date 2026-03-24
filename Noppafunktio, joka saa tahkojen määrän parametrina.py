import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))
maksimi = int(input("Anna tavoiteltava maksimisilmäluku: "))

silmaluku = 0

while silmaluku != maksimi:
    silmaluku = heita_noppaa(tahkot)
    print("Heitto:", silmaluku)