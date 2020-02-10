import os

# собирает
directory = './files'

files = os.listdir(directory)


for i in range(len(files)):
    print(files[i] + '    to >>>>>>    ' + str(i) + files[i][2:])
    os.rename(('./files/' + files[i]), ('./files/' + str(i) + files[i][2:]))
    i += 1

directory = './files'

files = os.listdir(directory)
print(files)
for i in range(10):
    print(files[i] + '    to >>>>>>    ' + str(i) + files[i][2:])
    os.rename(('./files/' + files[i]), ('./files/' + '0' + files[i]))
    i += 1
