# Leg uit wat stapsgewijze verfijning is. Illustreer met een voorbeeld.

# Antwoord:
# Stapsgewijze verfijning betekend dat we een groter probleem gaan opdelen in verschillende deelproblemen en deze apart gaan oplossen. Bij elke stap gaan we dus ons probleem opsplitsen.
# Concreet betekend dit voor python dat we een programma gaan opdelen door middel van verschillende functies te gebruiken, die samen het probleem oplossen.

# voorbeeld:
# stel we nemen een simpel voorbeeld waar we een programma moeten maken dat a^3+b^3 berekent.

# we kunnen dit doen door simpelweg dit te schrijven:
a = 3
b = 4
result = a ** 3 + b ** 3


# We kunnen echter ook stapsgewijze verfijning gebruiken en dit probleem opdelen in functies:

def main():
    a = 3
    b = 4
    print(som_derdemachten(a, b))


def som_derdemachten(k, i):
    return derde_macht(k) + derde_macht(i)


def derde_macht(n):
    n *= n * n
    return n


main()
