def count_power_of_five(n, sequence):
    count = 0

    for num in sequence:
        if is_power_of_five(num):
            count += 1

    return count

def is_power_of_five(num):
    while num % 5 == 0 and num > 1:
        num /= 5

    return num == 1

# Пример использования
n = 6
sequence = [1, 5, 25, 7, 30, 125]

power_of_five_count = count_power_of_five(n, sequence)
print("Количество степеней пятерки: ", power_of_five_count)