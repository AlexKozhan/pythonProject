x=input("Введите предложение - ")
n1=int(input("n1 = "))
n2=int(input("n2 = "))
if n1<=n2 and n2<len(x):
    b=x[:n1]+x[n2+1:]
    print(b)
else:
    print("failure")
