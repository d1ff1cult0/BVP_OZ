"""
Schrijf een recursieve functie die de som over een gegeven lijst gehele getallen
berekent. Gebruik geen iteratie, noch de ingebouwde functie om dit te berekenen.

Hint: Je mag wel de functie len gebruiken om te kijken hoeveel elementen je lijst
bevat.
"""

list_example = [3, 8, 16, 14, 12, 5, 10, 1]


def list_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + list_sum(list[1:])


print(list_sum(list_example))
if list_sum(list_example) == sum(list_example):
    print('Correct!')