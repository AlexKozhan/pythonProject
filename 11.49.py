m = [1, 4, -5, 3, 2]
for i in range(len(m)):
    if i<0:
        m[i] += m[1]
    else:
        m[i] += m[2]
print(m)