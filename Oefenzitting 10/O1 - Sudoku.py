# Implementeer een programma die een oplossing berekent
# voor mini-sudoku aan de hand van backtracking.

# Tip: Definieer helperfuncties en gebruik ze in je oplossing
# (bijvoorbeeld voor de kolom- en rijbeperkingen, of het bord een oplossing bevat, etc.).

# Extra: Breid je oplossing uit zodat je ook n × n-sudokus (met n gelijk aan 3, 4, 9, etc.)
# kan oplossen. (Voeg de subraster-beperking toe en pas je code aan zodat je borden van een
# willekeurig dimensie toelaat.)
sudoku = [[0, 2, 0],
          [3, 1, 0],
          [0, 3, 0]]

csudoku = [[1, 2, 3],
           [3, 1, 2],
           [2, 3, 1]]


def examine(partial_solution):
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    grootte_sudoku = len(sudoku)
    juiste_rijen = 0
    juiste_kolommen = 0
    dubbel = 0
    for i in range(len(partial_solution)):
        if len(partial_solution[i]) == len(set(partial_solution[i])):
            juiste_rijen += 1
        else:
            for k in range(1, len(partial_solution) + 1):
                if partial_solution.count(k) > 1:
                    dubbel += 1
        kolom = set()
        for j in range(len(partial_solution)):
            kolom.add(partial_solution[j][i])
        if len(kolom) == grootte_sudoku:
            juiste_kolommen += 1
        else:
            for k in range(1, len(partial_solution)+1):
                if partial_solution.count(k) > 1:
                    dubbel += 1
    if juiste_rijen == grootte_sudoku and juiste_kolommen == grootte_sudoku:
        return 'Accept'
    if dubbel > 0:
        return 'Abandon'
    else:
        return 'Continue'


def extend(partial_solution):
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    volgende_solutions = []
    psol = list(map(list, partial_solution))
    for i in range(len(psol)):
        for j in range(len(psol)):
            if psol[i][j] == 0:
                for k in range(1, len(psol)+1):
                    if k not in psol[i]:
                        k_not_in = 0
                        for m in range(len(psol)):
                            if psol[m][j] != k:
                                k_not_in += 1
                        if k_not_in == len(psol):
                            psol[i][j] = k
                            volgende_solutions.append(psol)
    return volgende_solutions

def solve(partial_solution):
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    exam = examine(partial_solution)
    if exam == 'Accept':
        print(partial_solution)
    elif exam != 'Abandon':
        for p in extend(partial_solution):
            solve(p)

solve(sudoku)