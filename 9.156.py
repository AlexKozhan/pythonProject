x="информация"
b="процессор"
mas=[]
for i in x:
    if i in b:
        mas.append("da")
    else:
        mas.append("net")
print(" ".join(mas))