import random as r
count=0
x=[]
for h in range(10):
    x.append(r.randint(-10,10))
    if x[h]==0:
        continue
print (x)
for i in range(len(x)-1):
    if x[i]*x[i+1]<0:
        count+=1
print(count)