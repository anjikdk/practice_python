from zipfile import *

f = ZipFile('G:/files.zip','w',ZIP_DEFLATED)
f.write('G:/test.txt')
f.write('G:/test1.txt')
f.write('G:/test2.txt')
f.close()
print("Files are ziped successfully...")