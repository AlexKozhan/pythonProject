x=input("введите слово - ")
if "a" in x and "o" in x:
    f1=x.index("a")
    f2=len(x)-x[::-1].index("o")-1
    y=list(x)
    y[f1]="o"
    y[f2]="a"
    y="".join(y)
    print(y)
else:
    print("что-то пошло не так")