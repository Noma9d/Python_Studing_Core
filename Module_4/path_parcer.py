import sys
from pathlib import Path

# Импорт из библиотеки 

def parse_folder(path):
    files = []
    folders = []
    
    for item in path.iterdir():    
        if item.is_dir():
            # print(item.name)
            folders.append(item.name)
            parse_folder(item)
        else:
            # print(item.name)
            files.append(item.name)
    return folders, files
if len(sys.argv[1])>0:
    path = Path(sys.argv[1])
else:
    path = Path(input())

print(parse_folder(path))