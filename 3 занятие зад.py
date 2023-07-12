a=int(input('Введите число'))
z=0
for i in range (1,7):
    b=int(input('ВВедите B'))
    if a*b<0:
        z+=1
    a=b
print (z)


