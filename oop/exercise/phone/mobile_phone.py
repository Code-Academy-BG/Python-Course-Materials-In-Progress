class NotExistingContact(ValueError):
    pass


class MobilePhone:
    def __init__(self, brand: str, year: int, material: str):
        self.brand = brand
        self.year = year
        self.material = material
        self.__contacts = {}

    @property
    def contacts(self):
        # shallow copy of contacts for user purposes
        return self.__contacts.copy()

    def call_contact(self, contact_name):
        if contact_name in self.__contacts:
            print(
                f"Calling to {contact_name}"
                f" - {self.__contacts[contact_name].number}"
            )
            self.__contacts[contact_name].update_times_dialed()
        else:
            print(f"There is no contact_id {contact_name}")

    def add_contact(self, number, name):
        if self.contact_exists(name):
            print("Contact already exists")
            return

        new_contact = Contact(number, name)
        try:
            self.__contacts[name] = new_contact
        except MemoryError:
            print("Not enough memory")
        else:
            print("Contact Saved")

    def contact_exists(self, contact_name):
        return contact_name in self.__contacts

    def get_contact_dial_count(self, contact_name):
        if not self.contact_exists(contact_name):
            raise NotExistingContact("Contact does not exists")
        return self.__contacts[contact_name].times_dialed

    def view_contacts(self):
        for key, contact in self.contacts.items():
            print(key, contact.name, contact.number)

    def __str__(self):
        return f"{self.brand}, {self.year}, {self.material}"


class Contact:
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name
        self.__times_dialed = 0

    @property
    def times_dialed(self):
        return self.__times_dialed

    def update_times_dialed(self):
        self.__times_dialed += 1

    def __str__(self):
        return f"{self.name} - {self.number}"


phone = MobilePhone("Nokia", 2002, "plastic")
phone.add_contact(12346789, "Pesho")
phone.add_contact(56798123, "Ivan")
phone.add_contact(56798123, "Stoyan")

phone.view_contacts()
phone.call_contact("Pesho")
print(phone.get_contact_dial_count("Pesho"))
