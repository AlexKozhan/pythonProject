a = int(input('введите a: '))
b = int(input('введите b: '))
if a <= b:
    for i in range (a, b+1, 1):
        print(i, end=" ")
else:
    print ('v')