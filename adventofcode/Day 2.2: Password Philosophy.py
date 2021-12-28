valid = 0
with open('2 input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = list(map(str, lines))
for i in lines:
    list = i.split()
    minmax = list[0]
    num1 = int(minmax.rpartition('-')[0]) + 1
    num2 = int(minmax.rpartition('-')[2]) + 1
    part1 = list[1]
    letter = part1.rpartition(':')[0]
    password = list[2]
    count = int(password.count(letter))

    if num2 > len(password):
        exit()
    if password[num1] == letter or password[num2] == letter:
        if password[num1] == letter and password[num2] == letter:
            valid = valid
        else:
            valid += 1

print(valid)
