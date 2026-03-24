def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


while True:
    gallonat = float(input("Anna bensiinin määrä nestegallonoina (negatiivinen lopettaa): "))

    if gallonat < 0:
        break

    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa = {litrat:.3f} litraa")