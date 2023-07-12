from math import sqrt
n = 50
result = 0
for i in range(n, 0, -1):
    result = sqrt(i + result)
print(f"Сумма равна: {result}")