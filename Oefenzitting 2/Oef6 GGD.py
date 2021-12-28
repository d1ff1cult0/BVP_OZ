a = int(input('Geef getal a: '))
b = int(input('Geef getal b: '))

while a != b:
    if a > b:
        a = a-b
    if b > a:
        b = b-a
if a == b:
    print(f'De grootste gemeenschappelijke deler is {a}.')