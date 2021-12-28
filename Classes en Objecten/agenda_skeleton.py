"""
    Klas Entry die een tijdsblok voorstelt in een agenda.
    Deze notitie heeft als attributen een dag, een start uur, een eind uur en een beschrijving van wat er geplant is.
"""


class Entry:

    # Initialiseer een entry met de gegeven parameters.
    def __init__(self, description="", day=1, start=0, end=23, location=""):
        self.description = description
        self.day = day
        self.start = start
        self.end = end
        self.location = location

    def get_description(self):
        return self.description

    def get_day(self):
        return self.day

    def get_start_slot(self):
        return self.start

    def get_end_slot(self):
        return self.end

    def get_location(self):
        return self.location

    def is_equal(self, other):
        if self.description == other.description and self.day == other.day and self.start == other.start and self.end == other.end and self.location == other.location:
            return True
        else:
            return False

    def set_description(self, description):
        self.description = description

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def is_valid_slot(self):
        if -1 < self.start < 24:
            return True
        else:
            return False

    def occupies_slot(self, uur):
        if self.start <= uur <= self.end:
            return True
        else:
            return False

    def overlaps_with(self, act2):
        if self.day == act2.day:
            if act2.start <= self.start <= act2.end:
                return True
            elif self.start <= act2.start <= self.end:
                return True
            else:
                return False
        else:
            return False

    def set_location(self, location):
        self.location = location

    # OVERLOADED OPERATIONS

    """
        Deze methode zorgt ervoor dat je str() kan gebruiken op een entry object.
        str() geeft een string terug met daarin de descriptie van de entry, de dag, start datum en eind datum.
        Als er een locatie is zal deze ook worden toegevoegd aan de string.
    """

    def __str__(self):
        """
        Return the textual representation of self.
        """
        string = self.get_description() \
                 + ' on ' + str(self.get_day()) \
                 + " from " + str(self.get_start_slot()) \
                 + " until " + str(self.get_end_slot())
        if len(self.get_location()) != 0:
            string += " at " + self.get_location()
        return string

    """
        Deze methode zorgt ervoor dat == kan gebruikt worden op 2 entry objecten bijvoorbeeld: entry1 == entry2.
        Om deze methode te laten werken moet eerst de is_equal methode geïmplementeerd worden
    """

    def __eq__(self, other):
        return self.is_equal(other)

    def __ne__(self, other):
        return not self.is_equal(other)


"""
    Klas Agenda die een agenda voorstelt.
    Deze klas houdt alle entries bij van deze agenda.
"""


class Agenda:

    # OVERLOADED OPERATIONS

    """
        deze methode zorgt ervoor dat je str() kan roepen met een agenda object,
        en dit geeft een string terug die je kan printen.
    """
    def __init__(self):
        self.entries = []

    def add_entry(self, app):
        if app not in self.entries:
            self.entries.append(app)
            return True
        else:
            return False

    def get_entries(self):
        return self.entries

    def remove_entry(self, entry):
        if entry in self.entries:
            self.entries.remove(entry)

    def get_entries_on_day(self, day):
        entries_on_day = []
        for act in self.entries:
            if act.day == day:
                entries_on_day.append(act)
        return entries_on_day

    def __str__(self):
        """
            Returns a chronologically ordered textual representation of the agenda.
        """
        string = ''
        for e in sorted(self.get_entries(), key=lambda entry: (entry.get_day(), entry.get_start_slot())):
            string += str(e) + '\n'
        return string


# STEP 1
entry = Entry(description="Methodiek van de informatica")
assert entry.get_description() == "Methodiek van de informatica"

# STEP 2
entry = Entry(day=200)
assert entry.get_day() == 200

# STEP 3
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert meeting.get_description() == "Dinner"
assert meeting.get_day() == 133
assert meeting.get_start_slot() == 18
assert meeting.get_end_slot() == 22

# STEP 4
meeting = Entry(description="Dinner", day=133, start=18, end=22)
for slot in range(0, 18):
    assert not meeting.occupies_slot(slot)
for slot in range(18, 23):
    assert meeting.occupies_slot(slot)
assert not meeting.occupies_slot(23)
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert not meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=12, end=13)
assert meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=13, end=14)
assert not meeting.overlaps_with(meeting2)

# STEP 5
agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert agenda.add_entry(meeting)
assert not agenda.add_entry(meeting)
assert len(agenda.get_entries()) == 1

agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
meeting3 = Entry(description="Breakfast", day=41, start=8, end=8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
assert len(agenda.get_entries_on_day(133)) == 1
assert len(agenda.get_entries_on_day(41)) == 2

# STEP 6
meeting = Entry()
meeting2 = Entry()
assert meeting == meeting2
assert not meeting != meeting2
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert meeting != meeting2
assert not meeting == meeting2

# STEP 7
agenda = Agenda()
meeting = Entry(description="Breakfast", day=41, start=8, end=8)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
meeting3 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.remove_entry(meeting3)
assert len(agenda.get_entries()) == 1
meeting4 = Entry(description="Dinner", day=133, start=18, end=22)
agenda.remove_entry(meeting4)
assert len(agenda.get_entries()) == 1

# STEP 8
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert meeting.get_location() == ""
meeting.set_location("De Volle Pollepel")
assert meeting.get_location() == "De Volle Pollepel"
meeting.set_location("")
assert meeting.get_location() == ""

# STEP 9
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert str(meeting) == "Dinner on 133 from 18 until 22"
meeting.set_location("De Volle Pollepel")
assert str(meeting) == "Dinner on 133 from 18 until 22 at De Volle Pollepel"

# STEP 10
agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
meeting3 = Entry(description="Breakfast", day=41, start=8, end=8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
assert str(agenda) == "Breakfast on 41 from 8 until 8\nLunch on 41 from 12 until 13\nDinner on 133 from 18 until 22\n"

print("OK.")
