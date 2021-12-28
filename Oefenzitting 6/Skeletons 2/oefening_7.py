"""
 In een bevraging moeten voetbalfans hun 3 
 favoriete voetbalteams kiezen (volgorde speelt geen rol). 
 De mogelijkheden zijn: "Bel", "Eng",“Ger", “Fra", 
 “Ita", “Spa" and “Cam". De resultaten zijn opgeslagen 
 in het bestand survey.txt. Zoek het antwoord op de 
 volgende vragen:
1. print de teams die door geen enkele fan gekozen zijn.
2. print het totaal aantal fans van wie zowel "Bel" als "
   Ger" een favoriet is.
3. maak een dictionary waarin je kan opzoeken 
   hoeveel fans voor elke combinatie van drie 
   teams hebben gekozen.
Hint: Je kan de volgende code gebruiken voor het lezen van informatie uit het bestand:
file=open("survey.txt","r") #hiermee open je het bestand enkel om het te lezen
for line in file.readlines(): # hiermee lees je het bestand lijn per lijn
	line=line.strip() # hiermee verwijder je het newline character	
	#hier kan je de lijn gebruiken in een functie
file.close() # sluit de file
"""

file = open("survey.txt", "r")
array = []
for line in file.readlines():
    line = line.strip()
    array.append(line)


def team_combinaties(lijst):

    #oef1
    team_list = ['Bel', 'Eng', 'Fra', 'Ita', 'Spa', 'Cam']
    dict_teams = {'Bel':'0','Eng':'0','Fra':'0','Ita':'0','Spa':'0','Cam':'0',}
    for i in range(len(lijst)):
        for j in range(len(team_list)):
            if lijst[i].find(team_list[j]) != -1:
                temp = int(dict_teams[team_list[j]])+1
                dict_teams[team_list[j]] = f'{temp}'
    for i in range(len(dict_teams)):
        niet_gekozen = []
        if dict_teams[team_list[i]] == '0':
            niet_gekozen.append(team_list[i])
    print(niet_gekozen)

    #oef2
    BelGer = 0
    for i in range(len(lijst)):
        if lijst[i].find('Ger') != -1 and lijst[i].find('Bel') != -1:
            BelGer += 1
    print(BelGer)

    #Oef 3
    dict = {}
    for i in range(len(lijst)):
        if lijst[i] in dict:
            temp = int(dict[lijst[i]])+1
            dict[lijst[i]] = f'{temp}'
        else:
            dict[lijst[i]] = '1'
    print(dict)


team_combinaties(array)
file.close()



