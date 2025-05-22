import os

root = os.getcwd()
disorganized_path = f'{root}/disorganizedFiles'

files = os.listdir(disorganized_path)


for file in files:
    while os.path.isdir(file):
        pass
    extension = file.split('.')[1].upper()
    print(extension)

