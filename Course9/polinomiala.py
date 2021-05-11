# 2x^4 + 0x^3 + 3x^2 - 5x^1 + 5x^0


class Polinomiala:
    def __init__(self, *args):
        self.coefs = args

    def __repr__(self):
        rez = ''
        power = 0
        for i in self.coefs[::-1]:
            # if i > 0:
            #     rez += f' + {i}x^{power}'
            # else:
            #     rez += f' {i}x^{power}'
            rez += f' + {i}x^{power}'
            power += 1
        rez = rez.replace('+ -', '+ ')
        rez = rez[3:]
        return rez


p1 = Polinomiala(3, 0, 2, -5, 1)
print(p1.coefs)
print(p1)