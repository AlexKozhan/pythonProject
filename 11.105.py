import random
x = []
count=0
previous = random.randint(1, 10)
x.append(previous)
print (x)
for _ in range(29):
    current = random.randint(previous, previous + 5)
    x.append(current)
    previous = current
print("Неубывающая последовательность:", x)
for i in range(len(x)):
    if x[i]!=x[i-1]:
        count+=1
print (count)