print ('Cреднее арифметическое по блок-схеме. \n')

numbers =[2, 5, 13, 7, 6, 4]
size = 6
sum = 0
avg = 0
index = 0

print ('Исходный массив: ', numbers)

while index<size:
    sum = sum + numbers[index]
    index =index+1
avg=sum/size

print("\nСреднее арифметическое = ", avg)