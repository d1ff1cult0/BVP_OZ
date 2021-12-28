n = int(input('How many numbers will you give: '))
even = False
divby3 = 0
for i in range(n):
    number = int(input(f'Give number {i + 1}: '))
    if number % 2 == 0:
        even = True
    if number % 3 == 0:
        divby3 += 1
if even:
    print(f'You gave an even number!')
print(f'You gave {divby3} numbers that are divisible by 3!')
