n = int(input('введите n - '))
a=1

print("Последовательность чисел a, a1, a2, ..., an:")
print("a =", a)

for k in range(1, n+1):
    a = a + 1/k
    print(f"a{k} =", a)