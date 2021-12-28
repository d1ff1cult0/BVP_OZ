""""
Vind de quadrupels (a,b,c,d) die voldoen aan de gelijkheid a^3+b^3 = c^3+d^3 voor waarden van a, b, c,
d in het interval [1,15]. Gebruik hiervoor een list comprehension en zorg ervoor dat er geen triviale oplossingen
gevonden worden, zoals a = c en b = d, of a = d en b = c.

Als uitbreiding kan je kijken of je gelijkenissen ziet tussen je oplossingen. Kan je je algoritme aanpassen zodat het
maar één antwoord geeft?
"""
interval = [i for i in range(1, 15)]
solutions = []
i = 0

for a in interval:
    for b in interval:
        for c in interval:
            for d in interval:
                if a != c and b !=d:
                    if a != d and b != c:
                        if a**3+b**3 == c**3+d**3:
                            if a < b and d > c > a:
                                temp = [a, b, c, d]
                                solutions.append(temp)

print(solutions)

