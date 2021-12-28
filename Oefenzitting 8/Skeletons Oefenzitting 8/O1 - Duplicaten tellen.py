"""
Hieronder  vind  je  verschillende  algoritmes  om  na  te  gaan  of  een  lijst  al  dan  niet  duplicaten bevat.
Het is aan jou om na te gaan wat de tijdscomplexiteit van deze verschillende versies is, voor zowel het ‘worst case
scenario’ als voor het ‘best case scenario’. Op Toledo vind je dezelfdecode ook terug in een.py-bestand.

Hint: Schrijf je notities in commentaar naast de code, zo behoud je een goed overzicht van je gedachteproces.
"""


#best case: eerste element is gelijk aan 2de element
#worst case: er zijn geen duplicaten


#n = len(lst)
def has_duplicates_v1(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                return True
    return False

# O(n^2)
#Best case -> O(1)
#Worst case -> O(len(list)^2)


###############################################################################


def has_duplicates_v2(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
# O(n)*O(n-1)
#-> O(n^2-n)
#-> O(n^2) -> want grote orde
#Best case -> O(1)
#Worst case -> O(n^2)

###############################################################################


def has_duplicates_v3(lst):
    found_duplicate = False
    i = 0
    while i != len(lst):
        if lst.count(lst[i]) > 1:
            found_duplicate = True
        i += 1
    return found_duplicate

#O(n^2)
#Best case -> O(1)
#Worst case -> O(len(lst)^2)


###############################################################################


def has_duplicates_v4(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i + 1:]:
            return True
    return False
#O(n^2)
#Best case -> O(1)
#Worst case -> O(len(lst)^2)

###############################################################################


def has_duplicates_v5(lst):
    already_seen = {}
    for x in lst:
        if x in already_seen:
            return True
        already_seen[x] = True
    return False
#O(n^2)
#Best case -> O(1)
#Worst case -> O(len(lst)^2)


###############################################################################


def has_duplicates_v6(lst):
    return len(set(lst)) < len(lst)
# O(1)