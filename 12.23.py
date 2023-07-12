import random as r
mas = []
for i in range(7):
    mas.append([])
    for j in range(7):
        mas[i].append(0)
for i in range(7):
    print(mas[i])
for i in range(7):
    for j in range(7):
        if i==j or i+j==len(mas)-1:
            mas[i][j]=1
print()
for i in range(7):
    print(mas[i])