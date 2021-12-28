"""
Schrijf een programma dat de alternerende som van elementen in een lijst
berekent. Je mag de invoer hier direct in een variabele plaatsen en hoeft deze dus niet op te vragen aan de gebruiker.

Bijvoorbeeld bij de lijst [1, 4, 9, 16, 9, 7, 4, 9, 11] berekent het programma 1 - 4 + 9 - 16 + 9 - 7 + 4 - 9 + 11 = -2.
"""
list = [1,4,9,16,9,7,4,9,11]
result = 0
for i in range(len(list)):
    if i%2 != 0:
        list[i] *= -1
    result += list[i]
print(result)
