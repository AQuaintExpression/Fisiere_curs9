class A:
    pass

class B:
    def __init__(self, lst_info):
        self.lst_info = lst_info

    def show_info(self):
        for elem in self.lst_info:
            print(elem)


a1 = A()
a2 = A()
a3 = A()
a4 = A()

b = B([a1, a2, a3, a4])
b.show_info()
