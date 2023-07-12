import random as r
count=0
x=[]
for h in range(20):
    x.append(r.randint(0,100))
    if x[h]<=x[h-1]:
        continue
print (x)
for i in range(1,len(x)):
    if x[h]==x[h-1]:
        count+=1
v=20-(count*2)
print(count, v)
