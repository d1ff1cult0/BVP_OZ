set1 = {2, 3, 4, 8, 10, 1, 0}
set2 = {5, 4, 11, 0}


def set_merger(x, y):
    result = x.symmetric_difference(y)
    print(result)


set_merger(set1, set2)