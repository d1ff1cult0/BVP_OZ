"""
Schrijf een functie interpret die eenvoudige  commando’s inleest en uitvoert.
Er zijn twee soorten commando’s:
    "add x y": tel x en y op, met x en y reële getallen.
    "subtract x y": trek y af van x, met x en y reële getallen.

De functie moet altijd een reëel getal teruggeven. Schrijf ook zelf een main-functie
waarin je je interpreter test door invoer op te vragen aan de gebruiker tot deze
"stop" ingeeft, samen met enkele assert statements.

Hint: Gebruik de split-functie om een string op te splitsen in verschillende delen.
"""


def calculator(command):
    command_list = command.split()
    if command_list[0] == 'add' or command_list[0] == 'subtract':
        if command_list[0] == 'add':
            return int(command_list[1]) + int(command_list[2])
        if command_list[0] == 'subtract':
            return int(command_list[1]) - int(command_list[2])
    if command_list[0] == 'stop':
        exit()
    else:
        return "Dit is geen geldig commando, gelieve 'add' of 'subtract' te gebruiken"


def main():
    assert calculator('add 17 3') == 20
    assert calculator('add 12 9') == 21
    assert calculator('add 8 7') == 15
    assert calculator('subtract 18 7') == 11
    assert calculator('subtract 22 19') == 3
    assert calculator('subtract 18 36') == -18
    command = input('Geef het commando: ')
    while command[0] != 'stop':
        print(calculator(command))
        command = input('Geef het commando: ')


main()
