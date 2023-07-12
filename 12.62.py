import random as r
mas = []
s=0
for i in range(5):
    mas.append([])
    for j in range(7):
        mas[i].append(r.randint(0,10))
for i in range(len(mas)):
    print(sum(mas[i]))
for i in range(len(mas)):
    print(mas[i])
