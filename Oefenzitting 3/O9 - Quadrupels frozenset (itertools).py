""""
Vind de quadrupels (a,b,c,d) die voldoen aan de gelijkheid a^3+b^3 = c^3+d^3 voor waarden van a, b, c,
d in het interval [1,15]. Gebruik hiervoor een list comprehension en zorg ervoor dat er geen triviale oplossingen
gevonden worden, zoals a = c en b = d, of a = d en b = c.

Als uitbreiding kan je kijken of je gelijkenissen ziet tussen je oplossingen. Kan je je algoritme aanpassen zodat het
maar één antwoord geeft?
"""
from itertools import product, combinations

interval = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
solutions = set()
# with a != b and c != d enforced
for a, b, c, d in combinations(interval, r=4):
    print(a, b, c, d)
    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
        left_side = frozenset({a, b})
        right_side = frozenset({c, d})
        equality = frozenset({left_side, right_side})
        solutions.add(equality)

print(solutions)

