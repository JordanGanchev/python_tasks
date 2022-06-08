from os import walk
from os import listdir
from  os .path import isdir, join


def directory_traversal(path, file_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), file_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in file_by_ext:
                file_by_ext[extension] = []
            file_by_ext[extension].append(element)
result = {}
directory_traversal('./', result)

for key, value in result.items():
    print(key, value)

#-----------------------------------

for root, dirs, files in walk('.'):
    print(root)
    print(dirs)
    print(files)


#--------------------------------------

result = {}
for _, _, files in walk('.'): # walk('.', topdown=False):
    for file in files:
        ext = file.split('.')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(file)

for key, value in result.items():
    print(key, value)