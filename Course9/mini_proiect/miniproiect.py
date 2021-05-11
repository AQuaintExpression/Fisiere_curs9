import os
import re
import shutil

class Memorie:
    def __init__(self, cache):
        self.cache = cache


class FileManager(Memorie):
    def __init__(self, cache):
        super().__init__(cache)

    #create_directory: primește ca parametru calea unui director ce va fi creat, dacă nu există.
    # Directorul nou creat va fi adăugat în cache.

    def create_directory(self, directory_path):
        try:
            os.mkdir(directory_path)
            self.cache[directory_path] = []
        except FileExistsError:
            print('The folder already Exists!!!')


    # ○ upload: primește ca parametru numele unui fișier, continutul pe care îl veți scrie în fișier,
    # respectiv calea directorului unde vreți să uploadați fișierul respectiv. Implicit se va actualiza
    # cache-ul cu noul fișier. În cazul în care directorul primit ca parametru nu există, acesta va fi creat.
    # Atentie la nesting folders (niv1/niv2).

    def upload(self, filename, content, file_path):
        try:
            os.makedirs(file_path)
        except FileExistsError:
            print('Folderul exista; Mergem mai departe')

        with open(f'{file_path}\\{filename}', 'w') as f:
            f.write(content)

        l = os.listdir(file_path)
        self.cache[file_path] = l


    #download: primește ca parametru numele unui fisier. Dacă acesta există în cache, atunci calea complete
    # (path+name) ii va fi afisata utilizatorului. In cazul in care exista mai multe fisiere cu acest nume,
    # dar care se afla in directoare separate, atunci veti afisa calea unuia dintre fisierele gasite.

    def download(self, filename):
        for key, value in self.cache.items():
            if filename in value:
                print(f'{key}\\{filename}')
                break


    #○ get_content: această metoda va afișa utilizatorului întreg conținutul din cache.
    # Ca să fie mai ușor de urmărit, puteți să afișați conținutul fiecărui director în parte.
    # ○ delete_directory: dându-se director, acesta va trebui șters de pe disk, dacă există.
    # De asemenea, cache va trebuie actualizat astfel încât să nu mai conțină acest director.
    # Atenție la directoarele care conțin fișiere sau alte sub-directoare.

    def get_content(self):
        for key in self.cache:
            print(key, '--', self.cache[key])

    def delete_directory(self, directory):
        import shutil
        try:
            shutil.rmtree(directory)
            del self.cache[directory]
        except FileNotFoundError:
            print('File not found')

    # get_files_by_name_regex: aceasta metoda va primi ca parametru un pattern și va returna lista de
    # fișiere care se potrivesc cu pattern-ul respectiv.

    def get_files_by_name_regex(self, pattern):
        lists = list(self.cache.values())
        rez = []
        for lst in lists:
            rez.extend(lst)
        rez = ' '.join(rez)
        p = re.compile(pattern)
        rez = p.findall(rez)
        return rez

    # get_files_by_content: aceasta metoda va avea 2 parametri: un string si un parametru default
    # regex_enabled setat ca False(implicit). Ea va returna o lista cu toate numele fisierelor in
    # care s-a gasit un match intre stringul dat ca parametru de intrare si continutul fisierului.
    # Daca regex_enabled este setat ca True functia va cauta patternul dat la intrare si va returna
    # o lista cu numele fisierelor unde s-a facut match.

    def get_files_by_content(self, string, regex_enabled=False):
        rez = []
        for dir_path, files in self.cache.items():
            for file in files:
                with open(f'{dir_path}\\{file}') as f:
                    data = f.read()
                if regex_enabled == False:
                    if string in data:
                        rez.append(file)
                else:
                    pattern = re.compile(string)
                    if pattern.search(data):
                        rez.append((dir_path, file))
        return rez

cache = {
    'dir': ['fisier1.txt'],
    'dir\\dir1': ['file.txt'],
    'dir\\dir1\\dir11': ['fisier.txt', 'fisier1.txt'],
    'dir\\dir1\\dir12': ['fisier2.txt'],
    'dir\\dir2': ['fisier.txt'],
}


fm = FileManager(cache)
# print(fm.cache)
# fm.create_directory('dir\\dir1\\dir14')
# print(fm.cache)

# print(fm.cache)
# fm.upload('fisier_uploadat.txt', 'Aceasta este o linie incarcata cu upload', 'dir\\dir1\\dir11')
# print(fm.cache)

# fm.download('fisier.txt')
# fm.get_content()

# print(fm.cache)
# fm.delete_directory('dir\\dir2')
# print(fm.cache)

# print(fm.get_files_by_name_regex(r'fisier[0-9]{0,}\.txt'))
print(fm.get_files_by_content(r'[0-9]{3,}', regex_enabled=True))
