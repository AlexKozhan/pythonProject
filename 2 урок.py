number = int(input("введите число: ")
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print ('факториал числа', number, 'равен', factorial)