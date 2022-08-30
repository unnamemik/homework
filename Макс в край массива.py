print ('Максимальное число в правый край массива. \n')

numbers =[2, 5, 13, 7, 6, 4]
size = 6
index = 0
max_idx=0
max=numbers[max_idx]

print ('Исходный массив: ', numbers)

while index<size:
    if numbers[index]>max:
        max_idx=index
        max=numbers[index]
    index =index+1

numbers[max_idx]=numbers[size-1]
numbers[size-1]=max

print("\nРезультат = ", numbers)