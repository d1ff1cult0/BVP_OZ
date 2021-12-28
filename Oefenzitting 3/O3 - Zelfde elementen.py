"""
Schrijf een programma dat voor twee lijsten aangeeft of ze dezelfde waarden
bevatten. Elementen die meerdere keren voorkomen moeten ook even vaak in
beide lijsten aanwezig zijn. Je mag de invoer hier direct in variabelen plaatsen
en hoeft deze dus niet op te vragen aan de gebruiker.

Hint: Je kan gebruik maken van de sort()-functie om de lijsten te sorteren.
Deze functie werkt enkel als al je elementen van hetzelfde datatype zijn!
"""
list1 = ['appel', 'brood', 'koek', 'melk', 'appel', 'karamel']
list2 = ['appel', 'brood', 'koek', 'melk', 'appel', 'karamel']
same = 0

list1.sort()
list2.sort()

if len(list2) < len(list1):
    list = list2
else:
    list = list1

for i in range(len(list)):
    if list1[i] == list2[i]:
        same += 1
    if same == len(list1) == len(list2):
        print('De 2 lijsten hebben dezelfde elementen')

