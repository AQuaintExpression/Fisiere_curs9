#polimorfism

class Document:
    def __init__(self, nume):
        self.nume = nume

    def show(self):
        print('Document generic')


class Pdf(Document):
    def show(self):
        print('Sunt un document PDF')

class Word(Document):
    def show(self):
        print('Sunt un document Word')

class Txt(Document):
    def show(self):
        print('Sunt un document TXT')

class Csv(Document):
    pass

p = Pdf('Python For Beginners')
w = Word('Examen final Python')
t = Txt('nr de tel')
c = Csv('mrnset data')


files = [p, w, t, c]
for file in files:
    print(file.nume)
    file.show()
    print('@@@@@@@@@@@@@')
