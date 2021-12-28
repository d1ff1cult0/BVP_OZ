"""
Schrijf een programma dat twee lijsten tot één samenvoegt, waarbij er afwisselend
een element van de eerste dan wel de tweede genomen wordt. Je mag de invoer hier
direct in een variabele plaatsen en hoeft deze dus niet op te vragen aan de gebruiker.

Stel dat we als invoer [1, 4, 9, 16] en [9, 7, 4, 9, 11] krijgen, dan wordt het resultaat [1, 9, 4, 7, 9, 4, 16, 9, 11].

Hint: Je kan gebruik maken van de max()-functie om de lengte van de langste lijst te vinden.
"""

list1 = [1, 4, 9, 16]
list2 = [9, 7, 4, 9, 11]
merged_list = []

if int(len(list2)) > int(len(list1)):
    bigger_list = list2
    smaller_list = list1
else:
    bigger_list = list1
    smaller_list = list2

for i in range(len(smaller_list)):
    merged_list.append(smaller_list[i])
    merged_list.append(bigger_list[i])


lenght_dif = int(len(bigger_list))-int(len(smaller_list))
merged_list.append(bigger_list[-lenght_dif])
print(merged_list)

