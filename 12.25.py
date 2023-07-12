ch=1
mas=[]
for i in range(12):
    mas.append([])
    for j in range(10):
        mas[i].append(0)
for j in range(0,10):
    for i in range(11,-1,-1):
        mas[i][j]=ch
        ch+=1
for i in range(len(mas)):
    print(mas[i])





