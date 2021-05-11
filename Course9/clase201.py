# recap

class Programator:
    def __init__(self, nume, prenume, varsta, limbaj='Python'):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.limbaj = limbaj
        self.email = f'{self.prenume}.{self.nume}@company.com'.lower()

    def print_info(self):
        print(self.nume, self.prenume, self.email)

    def mai_batran(self, other):
        if self.varsta > other.varsta:
            return True
        else:
            return False

    def __repr__(self): # este apelata la print si cand se cheama str
                        # trebuie intodeaua sa returneze ceva
        return f'{self.nume} {self.prenume} -- {self.limbaj}'


class Manager:
    def __init__(self, nume, prenume, varsta, lista_angajati):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.email = f'{prenume}.{nume}@company.com'.lower()
        self.lista_angajati = lista_angajati

    def __len__(self):
        return len(self.lista_angajati)


p1 = Programator('Gheorge', 'Ionut', 28)
print(p1.limbaj)
p2 = Programator('John', 'Doe', 58, 'Assembler')
p1.print_info()
p1.mai_batran(p2)

# print(p1)
info_p1 = str(p1)
print(p1)
m = Manager('Anton', 'George', 40, [p1, p2])
# print(m.lista_angajati)
print(len(m))
