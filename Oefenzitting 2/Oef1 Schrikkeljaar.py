year = int(input('Geef een jaar: '))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print('Dit is een schrikkeljaar!')
        exit()
    if year % 100 == 0 and year % 400 != 0:
        print('Dit is geen schrikkeljaar')
        exit()
    else:
        print('Dit is een schrikkeljaar!')
else:
    print('Dit is geen schrikkeljaar')
