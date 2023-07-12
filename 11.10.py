n=int(input('Введите n'))
x=[]
while n !=0:
    x.append(n%10)
    n//=10
x.reverse()
print (x)
