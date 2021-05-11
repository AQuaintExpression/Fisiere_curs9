class A:
    def show_a(self):
        print('SUNT O FUNCTIE DIN CLASA A')

class B:
    def __init__(self, lst_info):
        self.lst_info = lst_info

    def func(self, obj):
        obj.show_a()


a = A()
b = B([1, 2, 3])
b.func(a)

