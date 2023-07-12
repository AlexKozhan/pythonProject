x=input("введите слово - ")
tr=x[2]
last=x[-1]
if len(x)>=3:
    b=x[:2]+last+x[3:-1]+tr
    print(b)
else:
    print("too small")