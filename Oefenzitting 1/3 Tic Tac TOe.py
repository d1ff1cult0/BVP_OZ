odd_row = '+--+--+--+'
even_row = '|  |  |  |'

for i in range(1,8):
    if (i % 2) != 0:
        print(odd_row)
    if (i % 2) == 0:
        print(even_row)
