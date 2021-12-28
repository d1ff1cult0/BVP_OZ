valid = 0
with open('2 input') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = list(map(str, lines))
for i in lines:
    list = i.split()
    minmax = list[0]
    min = int(minmax.rpartition('-')[0])
    max = int(minmax.rpartition('-')[2])
    part1 = list[1]
    letter = part1.rpartition(':')[0]
    password = list[2]
    count = int(password.count(letter))
    if min <= count <= max:
        valid += 1

print(valid)



