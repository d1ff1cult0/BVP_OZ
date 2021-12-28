# Geschatte tijdsbesteding: 45 minuten

# Het programma hieronder telt het aantal keer dat de waarde 0 voorkomt
# in de gegeven lijst xs. Het plaatst het resultaat in variabele n.

# Je mag in je assert-opdrachten gebruik maken van de volgende functie:


def nb_zeros(list):
    return len([x for x in list if x == 0])


xs = [0, 1, 2, 5, 0, 3, 8, 7, 0, 4, 0, 2, 1]


def cor_1():
    i = 0
    n = 0
    assert i == 0 and n == 0 and len(xs) > 0
    while i < len(xs):
        if xs[i] == 0:
            n = n + 1
        else:
            pass
        i = i + 1
    assert n == nb_zeros(xs)

# Voorzie dit programma van een gepaste preconditie en postconditie en
# bewijs haar correctheid.

# Voorzie twee bewijzen: één waarbij je partiële correctheid bewijst,
# en één waarbij je totale correctheid bewijst.

# Partiële correctheid:


i = 0
n = 0
assert i == 0 and n == 0 and len(xs) > 0
assert i == len(xs[:i])
while i < len(xs):
    assert i == len(xs[:i]) and i < len(xs)
    if xs[i] == 0:
        n = n + 1
    else:
        pass
    i = i + 1
    assert i == len(xs[:i])
assert i == len(xs[:i]) and i >= len(xs)
assert n == nb_zeros(xs)

# Totale correctheid:

i = 0
n = 0
assert i == 0 and n == 0 and len(xs) > 0
assert i == len(xs[:i])
while i < len(xs):
    oude_variant = n-i
    assert i == len(xs[:i]) and i < len(xs) and oude_variant == n-i
    if xs[i] == 0:
        n = n + 1
    else:
        pass
    i = i + 1
    assert i == len(xs[:i])
assert i == len(xs[:i]) and i >= len(xs)
assert n == nb_zeros(xs)
