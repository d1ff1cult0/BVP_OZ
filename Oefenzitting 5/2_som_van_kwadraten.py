"""
Schrijf met behulp van een while lus een programma dat de som van de kwadraten van 1 t.e.m. n berekent.
Bewijs de correctheid.
"""

n = int(input('Geef n: '))
assert n >= 0 and type(n) == int


def sum_quadrats(getal):
    k = 1
    assert asserting_sum(k) == 1
    som = 0
    while k <= getal:
        assert k <= getal
        som += k ** 2
        assert som == asserting_sum(k)
        k += 1
    assert k == n+1 and som == asserting_sum(getal)
    assert som == asserting_sum(k-1)
    return som


def asserting_sum(getal):
    som = ((getal * (getal + 1) * ((2 * getal) + 1)) / 6)
    return som


assert asserting_sum(n) == sum_quadrats(n)
print(sum_quadrats(n))
