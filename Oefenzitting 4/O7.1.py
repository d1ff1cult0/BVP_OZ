list_a = [2, 3, 3, 6, 8, 11, 11, 12, 12, 12]
list_b = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 11, 12, 13]
sorted_list = []


def list_sorting(a, b):
    merged_list = list_a + list_b
    while merged_list:
        minimum = merged_list[0]
        for i in merged_list:
            if i <= minimum:
                minimum = i
        sorted_list.append(minimum)
        merged_list.remove(minimum)
    return sorted_list


print(list_sorting(list_a, list_b))
