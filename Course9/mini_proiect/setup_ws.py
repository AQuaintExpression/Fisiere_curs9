import os
import shutil

try:
    shutil.rmtree('dir')
except FileNotFoundError:
    print('Folder does not exist')

os.makedirs('dir/dir1/dir11')
os.makedirs('dir/dir1/dir12')
os.makedirs('dir/dir2')

def create_file(filepath, filename, content):
    with open(f'{filepath}/{filename}', 'w') as f:
        f.write(content)

create_file('dir', 'fisier1.txt', 'Ana are 32141 mere')
create_file('dir/dir2', 'fisier.txt', 'George are 123 kiwi')
create_file('dir/dir1', 'file.txt', 'one')
create_file('dir/dir1/dir11', 'fisier.txt', 'LINIE')
create_file('dir/dir1/dir12', 'fisier2.txt', 'test test\nAsta e o linie noua 123')



cache = {
    'dir': ['dir1', 'dir2', 'fisier1.txt'],
    'dir\\dir1': ['dir11', 'dir12', 'file.txt'],
    'dir\\dir1\\dir11': ['fisier.txt'],
    'dir\\dir1\\dir12': ['fisier2.txt'],
    'dir\\dir2': ['fisier.txt'],
}