s = 0
zn = 1
for i in range(1, 100,1):
    s += zn*1/ i
    zn *= -1
print(s)