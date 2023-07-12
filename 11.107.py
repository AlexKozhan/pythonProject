import random as r
x=[]
for i in range(10):
    x.append(r.randint(0,9))
print (x)
print (min(x))
print (max(x))
i = max(x)-min(x)
print (i)
b=x.index(max(x))
print (b)
c = x.index(min(x))
print(b, c)