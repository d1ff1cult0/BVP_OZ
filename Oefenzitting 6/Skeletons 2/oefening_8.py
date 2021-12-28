"""
Schrijf drie functies die als input twee 
strings heeft en als output respectievelijk:
1) een set met alle hoofdletters en kleine 
   letters die in beide strings zitten
2) een set met alle hoofdletters en kleine 
   letters die in geen van beide strings zitten
3) een set met alle niet-letter tekens 
   die in beide strings zitten
"""

string1 = 'Bonjour je suis ne kloot'
string2 = 'Bananen zijn lekker'
string3 = 'B.on/jouér banân$enùzijn;lekker'
string4 = '#je@suis §ène àkloot'


def characters(s):
    return [char for char in s]


def oef1(s1, s2):
    allebei = {''}
    for i in range(len(s1)):
        for j in range(len(s2)):
            if characters(s1)[i] == characters(s2)[j] and characters(s1)[i] != ' ':
                allebei.add(characters(s1)[i])
    allebei.pop()
    print(sorted(allebei))


def oef2(s1, s2):
    alfabet = 'abcdefghijklmopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    complement = set(characters(alfabet)) - set(characters(s1)).union(set(characters(s2)))
    print(sorted(complement))


def oef3(s1, s2):
    alfabet = 'abcdefghijklmopqrtsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = (set(characters(s1)).union(set(characters(s2)))) - set(characters(alfabet))
    print(result)


oef1(string1, string2)
oef2(string1, string2)
oef3(string3, string4)

