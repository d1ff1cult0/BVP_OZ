"""
Gegeven twee versies van het bubble sort-algoritme. Bereken de tijdscomplexiteit van beiden. Maakt het een
wezenlijk verschil welke versie je gebruikt? Presteren ze anders onder het `best case scenario' of het `worst case
scenario'?
"""


def bubble_sort_left_to_right_suboptimal(lst):
    sorted_until = 0
    while sorted_until != len(lst):
        index_min = len(lst) - 1
        while index_min != sorted_until:
            if lst[index_min - 1] > lst[index_min]:
                lst[index_min - 1], lst[index_min] = lst[index_min], lst[index_min - 1]
            index_min -= 1
        sorted_until += 1
    return lst
#n^2
#Best case (al gesorteerd) O(n)
#Worst case (volledig tegenovergesteld) _> n^2
def bubble_sort_left_to_right(lst):
    sorted_until = 0
    while sorted_until != len(lst):
        begin = len(lst) - 1
        end = begin + 1
        while begin != sorted_until:
            if lst[begin - 1] > lst[begin]:
                lst[begin - 1], lst[begin] = lst[begin], lst[begin - 1]
                end = begin - 1
            begin -= 1
        sorted_until = end
    return lst

#n^2-n
#-> n^2
#Best case: O   (n)
#Worst case: O(n^2)