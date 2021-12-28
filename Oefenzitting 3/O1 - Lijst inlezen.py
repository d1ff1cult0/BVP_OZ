"""
Schrijf een programma dat één voor één positieve gehele getallen inleest en ze aan een lijst toevoegt indien
het getal er nog niet in staat. Wanneer de lijst tien elementen bevat, wordt deze geprint en stopt het programma.
"""
number = int(input('Geef een nummer: '))
list = []
if len(list) == 0:
    list.append(number)
while 10 > (len(list)) and number >= 0:
    number = int(input('Geef een nummer: '))
    for i in range(len(list)):
        if number != list[i]:
            list.append(number)
            break
else:
    print(list)
