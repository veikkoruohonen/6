import math

def yksikkohinta(halkaisija_cm, hinta_euroa):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m ** 2
    return hinta_euroa / pinta_ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

yks1 = yksikkohinta(halkaisija1, hinta1)
yks2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yks1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {yks2:.2f} €/m²")

if yks1 < yks2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yks2 < yks1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat samanarvoisia yksikköhinnaltaan.")