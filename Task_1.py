# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
prime_fac = [9, 7, 5, 3, 2]
my_list = []
i = 0
while i <= len(prime_fac)-1:
    if num % prime_fac[i] == 0:
        my_list.append(prime_fac[i])
        num //= prime_fac[i]
    else:
        i += 1
my_list.append(num)
print(my_list)
