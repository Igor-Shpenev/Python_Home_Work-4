#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральную степень числа: '))
list_num = []
for _ in range(3):
    list_num.append(random.randrange(2, 9))
print(f'Рандомные коэффициенты: {list_num}')
print(s := str(f'{list_num[0]}*x**{k} + {list_num[1]}*x**{k} + {list_num[2]} = 0'))
with open('file.txt', 'w') as nomial:
    nomial.writelines(s)
