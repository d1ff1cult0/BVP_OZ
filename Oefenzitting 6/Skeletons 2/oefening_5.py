"""
In cryptografie is caesar cipher een encryptietechniek
waarin elke letter in het alfabet vervangen wordt door
een letter die een aantal posities verder in het alfabet 
staat. In dit geval implementeren we ROT-13, waarbij elke 
letter dertien plaatsen opschuift. Een a zou bijvoorbeeld 
een n worden. Schrijf hiervoor een encoder en decoder en 
vertaal/codeer hiermee de volgende twee berichten:
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
Gebruik voor deze opgave een dictionary!
"""


def ROT():
    zin = str(input('Geef een zin: '))
    zin = zin.lower()
    array = []
    dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
            'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
            ' ': ' ', '?': '?', '!': '!', '.': '.'}
    for i in range(len(zin)):
        array.append(dict[zin[i]])
    array = ''.join(array)
    return array


print(ROT())


