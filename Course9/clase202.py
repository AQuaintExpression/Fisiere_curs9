class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.email = f'{nume}.{prenume}@company.com'.lower()

    def mareste_salariu(self, raise_amount):
        self.salariu *= raise_amount

class Programator(Angajat):
    def __init__(self, nume, prenume, salariu, limbaj):
        super().__init__(nume, prenume, salariu)
        self.limbaj = limbaj

    # def mareste_salariu(self):
    #     super().mareste_salariu(1.10)

class Junior(Programator):
    def __init__(self, nume, prenume, salariu, limbaj, contract_temporar=True):
        super().__init__(nume, prenume, salariu, limbaj)
        self.contract_temporar = contract_temporar

    def func(self):
        super().mareste_salariu(2)



p1 = Programator('John', 'Doe', 7000, 'Python')
j = Junior('Smithy', 'Joe', 2000, 'Assembler')
print(j.salariu)
j.func()
print(j.salariu)