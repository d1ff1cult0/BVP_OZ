"""
Schrijf een functie die het minimum aantal munten berekent dat nodig is om een bepaald
bedrag te betalen. Het bedrag en een lijst met mogelijke muntwaarden worden als argumenten
meegegeven.

Als de invoerlijst [1, 2, 5, 10, 20, 50] is, is het minimum aantal munten dat nodig is om
een bedrag van 67 te betalen gelijk aan 4 (namelijk 50 + 10 + 5 + 2).

Veronderstel het volgende bij het schrijven van de functie:
    1. Het invoerbedrag is een positief geheel getal verschillend van nul.
    2. De functie veronderstelt een niet-lege lijst met mogelijke muntwaarden.
    3. Ga ervan uit dat het opgegeven bedrag altijd kan worden betaald met de munten uit de
    gegeven lijst met waarden.
"""
munten = [1, 2, 5, 10, 20, 50]
lijst = []

def examine(input, partial_solution):
    if len(partial_solution) > 5:
        return 'Abandon'
    if sum(partial_solution) == input:
        return 'Accept'
    elif sum(partial_solution)<input:
        return 'Continue'
    else:
        return 'Abandon'


def extend(input, partial_solution):
    possible_solutions = []
    for i in munten:
        temp_partial_solutions = partial_solution[:]
        temp_partial_solutions.append(i)
        possible_solutions.append(temp_partial_solutions)
    return possible_solutions


def solve(input, partial_solution):
    exam = examine(input, partial_solution)
    if exam == 'Accept':
        lijst.append(partial_solution)
    elif exam != 'Abandon':
        for p in extend(input, partial_solution):
            solve(input, p)


solve(67, [])

shortest = (lijst[0], len(lijst[0]))
for i in lijst:
    if len(i) < len(shortest[0]):
        shortest = (i, len(i))
print(shortest)