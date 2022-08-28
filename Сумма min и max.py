print('Инвертирование массива . \n Введите числа. По завершению нажмите ввод. \n')

nums = []

while True:
    elem = (input())
    if not elem:
        if elem == 0:
            continue
        else:
            break
    nums.append(elem)

print('Массив: ', nums)

sum = sum (nums[(min(nums)):(max(nums)):1])

print('Сумма: ', nums)
