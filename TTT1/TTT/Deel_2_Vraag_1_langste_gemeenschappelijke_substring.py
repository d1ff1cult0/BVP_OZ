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

# Deze functie berekent de langste gemeenschappelijke substring(s) van 2 strings
# Bv. de langste gemeenschappelijke substring van 'methodisch' and 'katholiek' is { 'tho' }
#
# Bemerk dat 2 strings verschillende gemeenschappelijke substring kunnen hebben die alle even
# lang zijn.
# Bv. de langste gemeenschappelijke subsequenties van 'programmeren' and 'ramsterrenbeeld' zijn
#       { 'ram', 'ren' }
#
# Als 2 strings geen gemeenschappelijke substring hebben, dan is de langste gemeenschappelijke
# subsequentie de lege string.
#
# @param xstr  - een string
# @param ystr  - een string
# @return      - een verzameling van de langste gemeenschappelijke substring(s) van xstr en ystr
#                zoals hierboven gedefinieerd

def langste_gemeenschappelijke_substring(xstr, ystr):
    langste_resultaat = ''
    kortste_string = ''
    langste_string = ''
    resultaat_array = []
    eind_resultaat = []

    if len(xstr) > len(ystr):
        kortste_string = ystr
        langste_string = xstr
    else:
        kortste_string = xstr
        langste_string = ystr

    for i in range(len(kortste_string)):
        for j in range(len(langste_string)):
            resultaat = ''
            k = 0
            while (i + k < len(kortste_string)) and (j + k < len(langste_string)) and kortste_string[i + k] == langste_string[j + k]:
                resultaat += langste_string[j + k]
                k += 1
            if len(resultaat) >= len(langste_resultaat):
                langste_resultaat = resultaat
                resultaat_array.append(langste_resultaat)

    for m in range(len(resultaat_array)):
        langst = len(resultaat_array[-1])
        if len(resultaat_array[m]) >= langst:
            eind_resultaat.append(resultaat_array[-1])
            eind_resultaat.append(resultaat_array[m])
    eind_resultaat = set(eind_resultaat)
    if len(eind_resultaat) == 0:
        return {''}
    return eind_resultaat





#
# DO NOT CHANGE ANYTHING BELOW THIS LINE !!!
#


def main():
    string1 = "aapje"
    string2 = "banaan"
    expected_result = {"aa"}
    result = langste_gemeenschappelijke_substring(string1, string2);
    print("Test met invoer |" + string1 + "| en |" + string2 + "|" + " geeft " + str(result))
    assert result == expected_result

    string1 = ""
    string2 = ""
    expected_result = {""}
    result = langste_gemeenschappelijke_substring(string1, string2);
    print("Test met invoer |" + string1 + "| en |" + string2 + "|" + " geeft " + str(result))
    assert result == expected_result



    string1 = "bvp"
    string2 = "pvb"
    expected_result = {"b", "p", "v"}
    result = langste_gemeenschappelijke_substring(string1, string2);
    print("Test met invoer |" + string1 + "| en |" + string2 + "|" + " geeft " + str(result))
    assert result == expected_result

    string1 = "methodiek"
    string2 = "ochtendgymnastiek"
    expected_result = {'iek'}
    result = langste_gemeenschappelijke_substring(string1, string2);
    print("Test met invoer |" + string1 + "| en |" + string2 + "|" + " geeft " + str(result))
    assert result == expected_result


#########################################################################################################
# VERANDER NIETS AAN DE LIJNEN HIERONDER, EN PLAATS ENKEL OPDRACHTEN BINNEN DE FUNCTIES HIERBOVEN
if __name__ == "__main__":
    main()
