"""
Schrijf een functie die twee reeds gesorteerde sequenties omzet naar één gesorteerde
sequentie die alle elementen van de reeksen bevat, inclusief duplicaten. Als een
element bijvoorbeeld tweemaal voorkomt in de eerste reeks en driemaal in de tweede,
zal de resultaatreeks dit element vijf keer moeten bevatten.

Je mag geen gebruik maken van de ingebouwde sort-functie. Gebruik het gegeven dat de
twee originele reeksen reeds gesorteerd zijn om dit probleem zelf door middel van
recursie op te lossen.
"""
list_a = [2, 3, 3, 6, 8, 11, 11, 12, 12, 12]
list_b = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 11, 12, 13]


def list_sorting():
    sorted_list = []
    if len(list_a) >= len(list_b):
        smaller_list = list_b
        bigger_list = list_a
        len_dif = len(list_a)-len(list_b)
    else:
        smaller_list = list_a
        bigger_list = list_b
        len_dif = len(list_b) - len(list_a)
    for i in range(len(smaller_list)):
        if smaller_list[i] == bigger_list[i]:
            sorted_list.append(smaller_list[i])
            sorted_list.append(bigger_list[i])
        if smaller_list[i] > bigger_list[i]:
            sorted_list.append(smaller_list[i])
            sorted_list.append(bigger_list[i])
        else:
            sorted_list.append(bigger_list[i])
            sorted_list.append(bigger_list[i])
    sorted_list.append(bigger_list[-len_dif:])
    return sorted_list


print(list_sorting())



