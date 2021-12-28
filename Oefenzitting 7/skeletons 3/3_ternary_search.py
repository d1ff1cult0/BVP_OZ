"""
Binary Search zoekt door een gesorteerde lijst in twee te splitsen en
vervolgens in slechts één helft verder te zoeken. Het Ternary Search
algoritme werkt analoog, maar zal de gesorteerde lijst in drie gelijke
delen splitsen. Implementeer een zoek algoritme om de index van een
gegeven waarde in een gesorteerde lijst te zoeken, gebruik makende van
het Ternary Search algoritme. Indien het element niet in de lijst
voorkomt, dan moet het algoritme -1 terug geven.
"""

from math import floor


def ternary_search(lijst, x, l, r):
    if r >= l:
        piv1 = l + (r - l) // 3
        piv2 = r - (r - l) // 3
        if lijst[piv1] == x:
            return piv1
        if lijst[piv2] == x:
            return piv2
        if lijst[piv1] > x:
            return ternary_search(lijst, x, l, piv1-1)
        if lijst[piv2] < x:
            return ternary_search(lijst, x, piv2+1, r)
        if lijst[piv1] < x < lijst[piv2]:
            return ternary_search(lijst, x, piv1+1, piv2-1)
    return -1


print(ternary_search([2, 2, 5, 7, 8, 11, 14, 15, 17, 18], 8, 0, 9))
# Tests om te kijken of de implementatie correct is
#assert ternary_search(8, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 4
#assert ternary_search(5, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 2
#assert ternary_search(17, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == 8
#assert ternary_search(12, [2, 2, 5, 7, 8, 11, 14, 15, 17, 18]) == -1