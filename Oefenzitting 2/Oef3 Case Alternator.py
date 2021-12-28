string = input('Geef een zin: ')
result = ""
i = 0
while i < len(string):
    index = string[i]
    if i % 2 == 0:
        result += index.upper()
    else:
        result += index.lower()
    i += 1
print(result)
