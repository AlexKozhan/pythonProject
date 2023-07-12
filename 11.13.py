import random as r
x=[]
for i in range(10):
    number =r.randint(0,13)
    x.append(number)
print (x)
b=int(input('введите индекс - '))
if b<len(x):
    s=x[b]
print(s)
