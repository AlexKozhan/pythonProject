#x=0
#for i in range(100, 501, 1):
  # x+=i
#print(x)

#a=int(input())
#for i in range(a, 501, 1):
  # a+=i
#print(a)

#b=int(input())
#for i in range(-10, b+1, 1):
   # b+=i
#print(b)

a=int(input())
b=int(input())
summ=0
if b>=a:
    for i in range(a, b+1, 1):
    summ+=i
    print(summ)
else:
    print ('введите другое b')