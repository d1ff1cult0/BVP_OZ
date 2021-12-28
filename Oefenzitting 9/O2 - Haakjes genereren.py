"""
Gegeven n, schrijf een functie die alle combinaties van n paren goed gevormde haakjes genereert
door gebruik te maken van backtracking. Hiermee wordt bedoeld dat elk openend haakje ook
terug gesloten wordt en vice versa. Voor n = 3 bijvoorbeeld, kunnen we als uitvoer de lijst
["((()))", "(()())", "(())()", "()(())", "()()()"] verwachten.
"""


def examine(input, partial_solution):
    if len(partial_solution) > 2*input:
        return 'Abandon'
    if len(partial_solution) == 2*input:
        l = 0
        r = 0
        for i in partial_solution:
            if i == '(': l+=1
            if i == ')': r+=1
            if r>l:
                return 'Abandon'
        if partial_solution.count('(') == partial_solution.count(')'):
            return 'Accept'
        else:
            return 'Abandon'
    else:
        return 'Continue'


def extend(input, partial_solution):
    possible_solutions = []
    for j in ['(', ')']:
        partial_solution_copy = partial_solution
        partial_solution_copy += j
        possible_solutions.append(partial_solution_copy)
    return possible_solutions


def solve(input, partial_solution):
    exam = examine(input, partial_solution)
    if exam == 'Accept':
        print(partial_solution)
    elif exam != 'Abandon':
        for p in extend(input, partial_solution):
            solve(input, p)


solve(3, '')