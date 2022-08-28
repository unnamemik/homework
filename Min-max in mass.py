print('Максимальное и минимальное число в массиве. \n Введите числа. По завершению нажмите ввод. \n')

mass = []
min_num = max_num = ''
array_length = 0
counter = 0

while True:
    elem = (input())
    if not elem:
        if elem == 0:
            continue
        else:
            break
    mass.append(elem)
    array_length += 1

print('Массив: ', mass)

array_length-=1
while array_length >= counter:
    if (min_num < mass[counter]):
        min_num = mass[counter]
    if (max_num > mass[counter]):
        max_num = mass[counter]
    counter += 1

print("Наибольшее число =  ", max_num, " наименьшее число = ", min_num)
