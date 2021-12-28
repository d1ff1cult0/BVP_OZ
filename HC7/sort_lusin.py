from helper_predicates import *
import random

def lusinvariant(values, orig_values, i):
    return is_sorted(values[:i]) and\
            is_permutation(values, orig_values) and\
            all_lte_all(values[:i], values[i:])

def minimum_position(values, start):
    min_pos = start
    i = start +1

    assert lte_all(values[min_pos], values[start:i])
    while i != len(values):
        assert lte_all(values[min_pos], values[start:i]
        if values[i] < values[min_pos]:
            min_pos = i

        i+= 1
        assert lte_all(values[min_pos, values[start:i]])
    assert lte_all(values[min_pos, values[start:i]])

def selection_sort(values):
    orig_values = values[:] #enkel nodig voor lusinvariant
    i =0

    assert lusinvariant(values, orig_values, i)
    while i != len(values):
        assert lusinvariant(values, orig_values, i)

        min_pos = minimum_position(values, i)
        values[i], values[min_pos] = values[min_pos], values[i]

