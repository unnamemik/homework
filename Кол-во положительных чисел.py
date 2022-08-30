print('Количество положительных чисел в массиве. \n')

numbers = [-2, 8, 14, -34, -9, 7, 7, 4]
size = 8
count = 0
index = 0

print ('Исходный массив: ', numbers)

while index < size:
    if numbers[index] > 0:
        count = count + 1
    index = index + 1

print('\nКоличество = ', count )
