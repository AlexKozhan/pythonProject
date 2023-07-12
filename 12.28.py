n=int(input("Input n "))
mas=[]
for i in range(n):
    mas.append([])
    for j in range(n):
        mas[i].append(0)
a=0
b=n-1
c=n-1
d=0
ch=1
while ch<=n*n:
    for i in range(d,b+1):
        mas[a][i]=ch
        ch+=1
    a+=1
    for i in range(a,c+1):
        mas[i][b]=ch
        ch+=1
    b-=1
    for i in range(b,d-1,-1):
        mas[c][i]=ch
        ch+=1
    c-=1
    for i in range(c,a-1,-1):
        mas[i][d]=ch
        ch+=1
    d+=1
for i in range(n):
    for j in range(n):
        print(mas[i][j],end="\t")
    print()