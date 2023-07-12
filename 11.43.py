import random as r
x=[]
for i in range(31):
    x.append(r.randint(0,9))
print(x)
for j in x:
    if j==0:
        print(f" {x.index(j) + 1}")
#Запись поглядеть