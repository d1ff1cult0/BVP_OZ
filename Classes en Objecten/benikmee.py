from _datetime import datetime
import time

class AgendaItem:
    def __init__(self, naam, beschrijving='/', duur=0, starttijd='2021-06-03 00:00:00', eindtijd='2021-06-04 01:12:18'):
        fmt = '%Y-%m-%d %H:%M:%S'
        assert duur >= 0
        self.naam = naam
        self.beschrijving = beschrijving
        self.duur = duur
        self.starttijd = datetime.strptime(starttijd, fmt)
        self.eindtijd = datetime.strptime(eindtijd, fmt)

    def geef_beschrijving(self):
        return f'Beschrijving: {self.beschrijving}'

    def geef_duur(self):
        duur = 0
        if self.duur > 0:
            duur = self.duur
        else:
            eindtijd_ts = time.mktime(self.eindtijd.timetuple())
            starttijd_ts = time.mktime(self.starttijd.timetuple())
            duur = int(((eindtijd_ts - starttijd_ts) / 60))

        return f'Duur: {duur} minuten.'

    def geef_naam(self):
        return f'{self.naam}:'

    def geef_starttijd(self):
        return f'Starttijd: {self.starttijd}'

    def geef_eindtijd(self):
        return f'Eindtijd: {self.eindtijd}'

    def pas_beschrijving_aan(self, beschrijving):
        self.beschrijving = beschrijving

    def pas_duur_aan(self, duur):
        assert duur >= 0
        self.duur = duur

    def pas_starttijd_aan(self, starttijd):
        fmt = '%Y-%m-%d %H:%M:%S'
        self.starttijd = datetime.strptime(starttijd, fmt)

    def pas_eindtijd_aan(self, eindtijd):
        fmt = '%Y-%m-%d %H:%M:%S'
        self.eindtijd = datetime.strptime(eindtijd, fmt)


les_BVP = AgendaItem('Les BVP')
les_BVP.pas_beschrijving_aan('Classes and Objects')
les_BVP.pas_starttijd_aan('2021-12-16 14:00:00')
les_BVP.pas_eindtijd_aan('2021-12-16 16:00:00')

def print_agendaitem(agenda_item):
    print(agenda_item.geef_naam())
    print(agenda_item.geef_beschrijving())
    print(agenda_item.geef_starttijd())
    print(agenda_item.geef_eindtijd())
    print(agenda_item.geef_duur())

print_agendaitem(les_BVP)
