import os
from datetime import datetime
import shutil

root = os.getcwd()
disorganized_path = f'{root}/disorganizedFiles'
organized_path = f'{root}/organizedFiles'

files = os.listdir(disorganized_path)


for file in files:
    extension = file.split('.')[1].upper()
    path = f'{organized_path}/{extension}'

    timestamp = os.path.getmtime(path)
    mod_date = datetime.fromtimestamp(timestamp).date()

    os.makedirs(path, exist_ok=True)

    complete_path = f'{path}/{mod_date}'
    os.makedirs(complete_path, exist_ok=True)

    origin = f"{disorganized_path}/{file}"
    destination = f'{complete_path}/{file}'

    shutil.move(origin, destination)
