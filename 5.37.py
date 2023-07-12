x=int(input('ВВедите x - '))
s = 1
for i in range(2, 12,1):
    s += i*x**(i-1)/i+1
    x *= -1
print(s)