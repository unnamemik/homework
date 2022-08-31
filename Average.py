print ('Cреднее арифметическое. \n Введите числа. По завершению нажмите ввод. \n')

num_list = []
S=i=k=0

while True:
        elem =(input())
        if not elem:
            if elem==0:
                continue
            else:
                break
        num_list.append(elem)
        i+=1
#print(num_list)
k=i
i-=1
while i>=0:
    S=S+float(num_list[i])
    i-=1
S=S/k
print("Среднее арифметическое = ", S)