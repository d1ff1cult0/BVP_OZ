import random
n = random.randint(0,20)
guess = int(input('Raad het getal tussen 0 en 20: '))
while guess != n and guess != -1:
    guess = int(input('Fout! Probeer nog een keer: '))
if guess == n and guess != -1:
    print('Proficiat, je hebt het getal geraden!')