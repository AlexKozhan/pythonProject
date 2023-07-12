import random as r
mas = []
s=0
for i in range(7):
    mas.append([])
    for j in range(7):
        mas[i].append(r.randint(0,10))
    print (mas[i])
s+=mas[3][j]#i это столбец (первая скобка строка, вторые стобец) из за массива вложенного
print(s)