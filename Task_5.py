#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

path = 'file2.txt'
data = open(path, 'r')
s = ''
for line in data:
    s += line
print(s.split(' '))
data.close()

path = 'file3.txt'
data = open(path, 'r')
s2 = ''
for line in data:
    s2 += line
print(s2.split(' '))
data.close()

