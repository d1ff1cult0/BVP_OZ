import random
import math

totaal_pogingen = int(input('Hoeveel pogingen?'))
in_cirkel = 0
pogingen = 0

while pogingen <= totaal_pogingen:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if math.hypot(x, y) <= 1:
        in_cirkel += 1
    pogingen += 1

pi = 4*in_cirkel/pogingen
print(in_cirkel, pogingen, pi)