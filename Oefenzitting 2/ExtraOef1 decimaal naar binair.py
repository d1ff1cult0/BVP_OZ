import math
number = int(input('Geef een decimaal getal: '))
k=[]
while number > 0:
    bit = int(float(number%2))
    k.append(bit)
    quotient = math.floor(number/2)
    number = quotient
print(k)