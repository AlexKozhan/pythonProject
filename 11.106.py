import random as r
count=0
max=0
x=[]
for h in range(10):
    x.append(r.randint(0,20))
print (x)
for i in range(len(x)):
    if x[i]%2==1 and x[i-1]%2==1:
        count+=1
        max=count
print (count)