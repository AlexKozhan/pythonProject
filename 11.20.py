import random as r
s=0
b=0
x=[]
for i in range(10):
    number =r.randint(0,10)
    x.append(number)
print(x)
while b < len(x):
    if b%2==0:
        s+=x[b]
    else:
        s-=x[b]
    b+=1
print(s)