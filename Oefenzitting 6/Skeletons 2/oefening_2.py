"""
Schrijf een programma dat als input een getal tussen 1 en 10 krijgt en als output dit getal voluit schrijft. Gebruik hiervoor een dictionary.
"""


def getal_voluit():
    getal = int(input('Geef een geheel getal tussen 1 en 10: '))
    getallen_voluit = {'1': 'één', '2': 'twee', '3': 'drie', '4': 'vier', '5': 'vijf', '6': 'zes', '7': 'zeven', '8': 'acht', '9': 'negen', '10': 'tien'}
    print(getallen_voluit[f'{getal}'])


getal_voluit()


