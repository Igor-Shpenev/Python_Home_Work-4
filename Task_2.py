#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
count = int(input('Введите кол-во элементов: '))

one_list = []
for _ in range(count):
    one_list.append(random.randrange(10, 20))
print(one_list)

new_list = []
for number in one_list:
    if one_list.count(number) == 1:
        new_list.append(number)
print(new_list)

