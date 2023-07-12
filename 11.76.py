import random as r
s=0
x=[]
for h in range(10):
    x.append(r.randint(0,100))
print(x)
for i in range(len(x)-1):
    if x[i]%2==0 and x[i+1]%2==0:
        s+=1
print (s)