'''
Implementeer de functies hieronder. Vervang daarvoor 'pass' door gepaste Python-code

Merk op!!
    Het bestand dat je uiteindelijk inzendt mag GEEN syntax-fouten meer bevatten!
    Inzendingen met syntaxfouten geven een 0-score, ook als die syntax-fouten in slechts 1
    functie voorkomen!
    Lukt het je niet om voor een bepaalde functie een oplossing te vinden? Zet dan (evt. een deel)
    van je code dat syntax-fouten kan bevatten in commentaar!

'''


#########################################################################################################

# Deze functie gaat na of een 2-dimensionale data-structuur leeg is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur
# @return   - True als m een lege lijst is (dus: [ ]), of slechts 1 element bevat dat op zich een lege lijst
#               is dus: [ [ ] ] );  anders False
def is_lege_matrix(m):
    if m == [] or m[0] == []:
        return True
    else:
        return False

#########################################################################################################

# Deze functie gaat na of de 2-dimensionale data-structuur een matrix is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur;
#             dit betekent dat als m niet leeg is, alle elementen van m een lijst zullen zijn
# @return   - True als alle 'rijen' van de data-structuur evenveel elementen bevatten, anders False
#           - bemerk: een lege matrix (zoals hierboven gedefinieerd in de functie
#               is_lege_matrix) is een matrix...


def is_matrix(m):
    if is_lege_matrix(m):
        return True
    else:
        lenght = len(m)
        row_lenght = len(m[0])
        same_lenght = 0
        if lenght == 1 and row_lenght == 0:
            return True
        else:
            for i in range(lenght):
                if len(m[i]) == len(m[0]):
                    same_lenght += 1
            if same_lenght == lenght:
                return True
            else:
                return False




#########################################################################################################


# Deze functie gaat na of alle elementen op de rand van een matrix gelijk zijn
# @param m  - de matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) matrix, zoals
#             hierboven gedefinieerd
# @return   - True als alle elementen op de rand van m gelijk zijn, anders False
#           - bemerk: de return-value van een lege matrix is True


def gelijke_rand_matrix (m):
    if is_lege_matrix(m):
        return True
    if is_matrix(m):
        rand_links_boven = m[0][0]
        lenght = len(m)-1
        row_lenght = len(m[0])
        totaal_correct_nodig = len(m[0]) + len(m[-1]) + ((len(m) - 2) * 2)
        correct = 0
        if lenght == 1 and row_lenght == 0 or (lenght == 0 and row_lenght == 0):
            return True
        else:
            for i in range(len(m)):
                if i == 0:
                    for j in range(len(m[0])):
                        if m[0][j] == rand_links_boven:
                            correct += 1
                        else:
                            return False
                if i == lenght:
                    for k in range(len(m[-1])):
                        if m[-1][k] == rand_links_boven:
                            correct += 1
                        else:
                            return False
                if i != 0 and i != lenght:
                    if m[i][0] == rand_links_boven:
                        correct += 1
                    if m[i][-1] == rand_links_boven:
                        correct += 1
            if correct == totaal_correct_nodig:
                return True
            else:
                return False
    else:
        return False


#########################################################################################################

# Deze functie maakt een nieuwe matrix met alle elementen van een oorspronkelijke matrix zonder de rand
# @param m  - de oorspronkelijke matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige, niet-lege matrix, zoals
#             hierboven gedefinieerd
# @return   - een matrix die alle elementen van m bevat zonder de rand-elementen
#           - bemerk: zie evt. de voorbeelden in de main-functie


def strip_matrix(m):
    if is_lege_matrix(m):
        return m
    else:
        nieuwe_matrix = m
        if len(m) == 1:
            nieuwe_matrix = [[]]
            return nieuwe_matrix
        for i in range(len(m)-1):
            if i == 0:
                nieuwe_matrix.pop(0)
                if is_lege_matrix(nieuwe_matrix):
                    return nieuwe_matrix
            if i == len(m)-1:
                nieuwe_matrix.pop(-1)
                if is_lege_matrix(nieuwe_matrix):
                    return nieuwe_matrix
            if is_lege_matrix(nieuwe_matrix):
                return nieuwe_matrix
            if i == 0:
                nieuwe_matrix[0].pop(0)
                nieuwe_matrix[0].pop(-1)
            if i != 0 and i != len(m):
                nieuwe_matrix[i].pop(0)
                nieuwe_matrix[i].pop(-1)
        return nieuwe_matrix


#########################################################################################################


# In deze functie worden de functies al voor enkele voorbeelden getest.
# Pas deze functie aan om eventueel zelf andere tests te definiëren.

def main ():
    print("-- is_lege_matrix --")

    assert is_lege_matrix([]) == True
    assert is_lege_matrix( [ [ ] ] ) == True
    assert is_lege_matrix( [ [1, 1] ] ) == False
    assert is_lege_matrix( [ [1, 2] ] ) == False

    print("-- is_matrix --")

    assert is_matrix( [ ] ) == True
    assert is_matrix( [ [ ] ] ) == True
    assert is_matrix( [ [1] ] ) == True
    assert is_matrix( [ [1, 'a'] ] ) == True
    assert is_matrix( [ [1, 'a'], [True, 1.2] ] ) == True
    assert is_matrix( [ [1, 'a'], [True, 1.2] , [ "hello"] ] ) == False

    print("-- gelijke_rand_matrix --")

    assert gelijke_rand_matrix( [ ] ) == True
    assert gelijke_rand_matrix( [[1, 'a'], [True, 1.2]]) == False
    assert gelijke_rand_matrix( [[1,   1,    1,  1 ],
                                [1, 1.2, True,  1 ],
                                [1,   1,    2,  1 ]]) == False
    assert gelijke_rand_matrix( [[1,   1,    1,  1 ],
                                [1, 1.2, True,  1 ],
                                [1,   1,    1,  1 ]]) == True
    assert gelijke_rand_matrix([ ['a',   'a',  'a',   'a' ],
                                ['a',   1.2, True,   'a' ],
                                ['a',     1,    1,   'a' ],
                                ['a',   'a',   'a',  'a']]) == True
    assert gelijke_rand_matrix( [['a',   'a',  'a',   'a' ],
                                ['a',   1.2, True,   'a' ],
                                ['a',     1,    1,   'a' ],
                                ['a',   'b',   'a',  'a']]) == False

    print("-- strip_matrix --")

    assert strip_matrix       ([['a',   'a',  'a',   'a' ],
                               ['a',   1.2, True,   'a' ],
                               ['a',     1,    1,   'a' ],
                               ['a',   'b',   'a',  'a']]) == [ [1.2, True], [1, 1] ]
    assert strip_matrix       ([['a',   'a',  'a',   'a' ],
                               ['a',   1.2, True,   'a' ],
                               ['a',   'b',   'a',  'a']]) ==  [ [1.2, True] ]
    assert is_lege_matrix(
            strip_matrix ([[1,   1,    1,  1 ]]) )
    assert is_lege_matrix(
                strip_matrix  ([['a', 'a', 'a', 'a'],
                               ['a', 'b', 'a', 'a']])
            )

#########################################################################################################
# VERANDER NIETS AAN DE LIJNEN HIERONDER, EN PLAATS ENKEL OPDRACHTEN BINNEN DE FUNCTIES HIERBOVEN
if __name__ == "__main__":
    main()