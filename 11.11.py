import random as r
x=[]
while len(x) <20:
    number=r.randint(0,50)
    if number not in x:
        x.append(number)
print(x)