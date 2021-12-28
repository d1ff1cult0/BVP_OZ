n = int(input('Geef getal: '))
faculteit = 1
counter = 1

while (counter <= n):
    faculteit = faculteit*counter
    counter += 1

print(f'Faculteit van {n} is {faculteit}')
