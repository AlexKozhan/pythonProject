def count_digits(number):
    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count

def compare_digit_counts(num1, num2):
    count1 = count_digits(num1)
    count2 = count_digits(num2)

    if count1 > count2:
        return f"Число {num1} содержит больше цифр, чем число {num2}"
    elif count1 < count2:
        return f"Число {num2} содержит больше цифр, чем число {num1}"
    else:
        return f"Число {num1} и число {num2} содержат одинаковое количество цифр"

# Пример использования
number1 = 12345
number2 = 6789

result = compare_digit_counts(number1, number2)
print(result)