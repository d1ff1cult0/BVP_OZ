"""
Schrijf een functie die, gegeven een lijst met unieke elementen, een lijst met alle mogelijke permutaties
teruggeeft. De volgorde van de uitvoer maakt niet uit. Bij invoer [1,2,3] zou je als resultaat [[1,2,3],[1,3,2],[2,1,3],
[2,3,1],[3,1,2],[3,2,1]] kunnen krijgen. Wat kan je doen als de elementen in de lijst niet uniek zijn?
"""


# Voel je vrij om bij de gegeven structuur argumenten naar keuze mee te geven!

def examine(input, partial_solution):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    element_in_both_lists = 0
    if len(set(partial_solution)) == len(partial_solution):
        for i in partial_solution:
            if i in input:
                element_in_both_lists += 1
        if element_in_both_lists == len(input):
            return 'Accept'
        else:
            return 'Continue'
    else:
        return 'Abandon'


def extend(input, partial_solution):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    possible_solutions = []
    for i in input:
        partial_solution_copy = partial_solution[:]
        if i in partial_solution_copy:
            pass
        else:
            partial_solution_copy.append(i)
            possible_solutions.append(partial_solution_copy)
    return possible_solutions


def solve(input, partial_solution):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(input, partial_solution)
    if exam == 'Accept':
        print(partial_solution)
    elif exam != 'Abandon':
        for p in extend(input, partial_solution):
            solve(input, p)


solve([1, 2, 3], [])
