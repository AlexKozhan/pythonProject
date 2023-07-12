x="1+2+3+4+5"
x=x.replace(" ","")
b=x.split("+")
summa=sum(int(i) for i in b)
print(summa)