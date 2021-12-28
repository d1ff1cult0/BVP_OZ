getal = int(input('Geef een potentieel priemgetal'))
i = 1
a = b = 0
while i <= getal:
    if getal % i == 0 and i != 1 and i != getal:
        a += 1
    else:
        b += 1
    i += 1
if a > 0:
    print('Het getal is geen priemgetal')
if a == 0 and b>0:
    print('Het getal is een priemgetal')
