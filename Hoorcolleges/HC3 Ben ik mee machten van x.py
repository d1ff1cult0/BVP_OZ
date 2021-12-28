float = float(input('Give a number: '))
power = int(input('Give a power: '))

for i in range(1, power+1):
    result = float**i
    print(result, end=" ; ")
'''Deze print dient om op volgende lijn te springen,
 want als er nog een andere print zou komen na het 
 printen van ons resultaat zou dit op dezelfde lijn komen'''
print()

