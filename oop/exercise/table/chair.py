from oop.principles.inheritance.person import PurePerson


class Chair:
    def __init__(self):
        self.is_free = True
        self.person = None

    @property
    def person_on(self):
        if not self.person:
            return None
        return self.person.name

    def sit_on(self, name):
        self.person = PurePerson(name)
        self.is_free = False

    def sit_off(self):
        self.person = None
        self.is_free = True
