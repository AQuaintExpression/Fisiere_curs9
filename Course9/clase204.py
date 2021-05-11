# metode abstracte

class FormaGeometrica:
    def calc_arie(self):
        raise NotImplementedError('Metoda trebuie implementata in clasa mostenitoare')

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def calc_arie(self):
        return self.latura ** 2

p = Patrat(5)
print(p.calc_arie())