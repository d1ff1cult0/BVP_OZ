"""
Schrijf een recursieve functie factoren die de ontbinding in priemfactoren van een
positief geheel getal berekent. Vermijd het gebruik van lussen.

Schrijf ook een main-functie waarin je je ontbindingsfunctie controleert op
correctheid door gebruik te maken van assert statements. Schrijf dus een main-functie
rond de aanwezige asserts en bedenk zelf nog twee andere.

Hint: Je kan lijsten concateneren door gebruik te maken van de + operator.
"""


def calc_factoren(n, f=2):
    if n < f:
        return []
    if n % f == 0:
        return [f] + calc_factoren(n / f, 2)
    return calc_factoren(n, f + 1)


print(calc_factoren(27))
