from math import sqrt
a = int(input(('Give A')))
b = int(input(('Give B')))
c = int(input(('Give C')))

sol1 = ((-b) + sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
sol2 = ((-b) - sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)

if b ** 2 - (4 * a * c) == 0:
    print(sol1)
if b ** 2 - (4 * a * c) < 0:
    print('Sorry, i cant calculate imaginary solutions')
else:
    print(f'The solutions are {sol1} and {sol2}')

