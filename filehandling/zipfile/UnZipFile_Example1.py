from zipfile import *

f = ZipFile('G:/files.zip', 'r', ZIP_STORED)
fileNames = f.namelist()
print(fileNames)
for name in fileNames:
    print("File name: ",name)
    print("Content of the file: ")
    f1 = open('G:/'+name, 'r')
    print(f1.read())
