"""
Schrijf met behulp van een while lus een programma dat n! berekent.
Bewijs de correctheid.
"""
from math import factorial as factorial

n = int(input('Geef n: '))
assert n >= 0 and type(n) == int


def faculteit(getal):
    fac = 1
    assert 1 == factorial(0)
    k = 1
    assert fac == factorial(k - 1)
    while k <= getal:
        oude_variant = n - k
        assert fac == factorial(k - 1) and k <= getal and oude_variant == n - k
        assert fac * k == factorial(k) and -1 <= n - (k + 1) < oude_variant
        fac *= k
        assert fac == factorial(k) and -1 <= n - (k + 1) < oude_variant
        k += 1
        assert fac == factorial(k - 1) and -1 <= n - k <= oude_variant

    assert fac == factorial(k - 1) and k > getal
    assert fac == factorial(getal)
    return fac


print(faculteit(n))
