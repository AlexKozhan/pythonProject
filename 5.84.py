n = int(input("Введите n "))
s = n ** 2
for i in range(n - 1, 0, -1):
    s = (s - i ** 2) ** 2
    print(f"значение выражения равно {s}")

