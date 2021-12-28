"""
Schrijf een programma dat, gegeven een lijst van positieve getallen, alle delen van deze lijst print
die strikt stijgend zijn. Zo zou het programma bij de invoer [1, 2, 3, 1, 2, 4, 8, 6] de deellijsten [1, 2, 3]}
en [1, 2, 4, 8] moeten tonen. Gebruik slicing om deze oefening op te lossen.
Je mag de lijst hier direct in een variabele plaatsen en hoeft deze dus niet op te vragen aan de gebruiker.
"""
import numpy as np
list = [1, 2, 3, 1, 2, 4, 8, 6]
new_list = []
breakpoint = float('inf')
for i in list:
    if i < breakpoint:
        temp = []
        new_list.append(temp)
    temp.append(i)
    breakpoint = i
print(new_list)
