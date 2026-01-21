from faker import Faker
faker = Faker("pl_PL")

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)
class BuisnessContact(BaseContact):
    def __init__(self, nawa_firmy, stanowisko, telefon_sluzbowy):
    

      super().__init__(imie, nazwisko, telefon, e_mail)
      self.nazwa_firmy = nazwa_firmy
      self.stanowisko = stanowisko
      self.telefon_sluzbowy = telefon_sluzbowy
        

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)
def create_contacts(rodzaj, ilosc):
    contacts = []

    for _ in range(ilosc):
        if rodzaj == "base":
            contacts.append(
                BaseContact(
                    faker.first_name(),
                    faker.last_name(),
                    faker.phone_number(),
                    faker.email(),
                )
            )

        elif rodzaj == "business":
            contacts.append(
                BusinessContact(
                    faker.first_name(),
                    faker.last_name(),
                    faker.phone_number(),
                    faker.email(),
                    faker.company(),
                    faker.job(),
                    faker.phone_number(),
                )
            )

    return contacts


