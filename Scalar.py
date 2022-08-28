import numpy as np

print("Скалярное произведение двумерных векторов", '\n')
quant = int(input('Введите количество векторов: '))

vect_x = []
vect_y = []
i = 0

while i < quant:
    print('\nВведите координату X', i + 1, '-го вектора: ')
    coor = int(input())
    vect_x.append(coor)
    print('Введите координату Y', i + 1, '-го вектора: ')
    coor = int(input())
    vect_y.append(coor)
    i += 1

print('\n', *vect_x, '  ', *vect_y, '\n')

vect_x=np.prod(vect_x)
print('\n', vect_x, '\n')
vect_y=np.prod(vect_y)
print('\n', vect_y, '\n')
sum = vect_x+vect_y

print('Скалярное произведение векторов равно: ', sum)