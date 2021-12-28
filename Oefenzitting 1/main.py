from math import sqrt
a = int(input('Geef a'))
b = int(input('Geef b'))
c = int(input('Geef c'))

det = ((b**2)-(4*a*c))
sol1 = ((-b)+sqrt(det))/(2*a)
sol2 = ((-b)-sqrt(det))/(2*a)

if det < 0:
    print('Sorry, ik kan geen complexe nulpunten vinden.')
if det > 0:
    print(f'De oplossingen zijn {sol1} en {sol2}')
if det == 0:
    print(sol1)