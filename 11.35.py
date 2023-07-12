import random as r
b=0
s=0
x=[]
for i in range(35):
    number =r.randint(0,10000)
    x.append(number)
print(x)
while b < len(x):
    s+=x[b]
    b+=1
print(s)
if s>=1000000:
    print('true')
else:
    print('false')