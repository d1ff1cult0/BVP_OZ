amount = int(input('Hoeveel elementen moet de reeks bevatten? '))
if amount<= 0:
   amount =  int(input('Gelieve een positief natuurlijk getal te nemen: '))
i = n = n1 = 0
n2 = 1
while i <= amount:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    i += 1