import numpy as np

print('Максимальное и минимальное число в массиве. \n Введите числа. По завершению нажмите ввод. \n')

mass = []

while True:
    elem = (input())
    if not elem:
        if elem == 0:
            continue
        else:
            break
    mass.append(int(elem))

print('Массив: ', mass, '\n')
max_num = max(mass)
min_num = min(mass)

print('Максимальное число = ', max_num)
print('Минимальное число = ', min_num, '\n')

min_index = mass.index(min_num)
max_index = mass.index(max_num)
diap_length = abs(min_index - max_index) - 1

if min_index < max_index:
    start = min_index+1
    stop = max_index
else:
    start = max_index+1
    stop = min_index

diap = mass[start:stop:]

print('Диапазон элементов : ', diap, '\n')
print('Сумма диапазона элементов = ', np.sum(diap))
