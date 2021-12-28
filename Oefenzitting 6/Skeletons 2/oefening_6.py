"""
 Schrijf een programma dat een set teruggeeft van 
 alle elementen die in beide sets voorkomen.
"""


def samen_in_set():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    result_set = set1.intersection(set2)
    return result_set


print(samen_in_set())