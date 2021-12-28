"""
Laat de gebruiker een string ingeven en print deze achterstevoren door gebruik te maken van slicing.
"""

string = 'BVP is het leukste vak van allemaal'
print(string[::-1])
wordlist = string.split()
wordlist_reverse = list(reversed(wordlist))
print(" ".join(wordlist_reverse))
