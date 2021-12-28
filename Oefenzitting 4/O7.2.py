list_a = [2, 3, 3, 6, 8, 11, 11, 12, 12, 12]
list_b = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 11, 12, 13]
merged_list = list_a+list_b


def list_sorting(x):
    if len(x) <= 1:
        return x
    else:
        return list_sorting([i for i in x[1:] if i <= x[0]]) + [x[0]] +\
               list_sorting([i for i in x[1:] if i > x[0]])


print(list_sorting(merged_list))