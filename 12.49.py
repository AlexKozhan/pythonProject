import random as r
mas = []
s=0
for i in range(3):
    mas.append([])
    for j in range(4):
        mas[i].append(r.randint(0,10))
    print (mas[i])
c=int(input())
for i in range(len(mas)):
    for j in range(len(mas[i])):
        if j==c:
            s=s+mas[i][j]**2
print(s)
for i in range(len(mas[1])):
    s=s+mas[1][i]**2
print(s)
