def count_even_odd(a, b):
    even_count = 0
    odd_count = 0

    for num in a:
        if is_even(num):
            even_count += 1

    for num in b:
        if is_odd(num):
            odd_count += 1

    return even_count, odd_count

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

# Пример использования
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [10, 11, 12, 13, 14, 15, 16, 17]

even_count, odd_count = count_even_odd(a, b)
print("Количество четных чисел в первой последовательности: ", even_count)
print("Количество нечетных чисел во второй последовательности: ", odd_count)