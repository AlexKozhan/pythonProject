#10.18
def get_digit_sum(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum

def compare_digit_sums(num1, num2):
    sum1 = get_digit_sum(num1)
    sum2 = get_digit_sum(num2)

    if sum1 > sum2:
        return f"Сумма цифр числа {num1} больше, чем сумма цифр числа {num2}"
    elif sum1 < sum2:
        return f"Сумма цифр числа {num2} больше, чем сумма цифр числа {num1}"
    else:
        return f"Сумма цифр числа {num1} и сумма цифр числа {num2} равны"

# Пример использования
number1 = 12345
number2 = 6789

result = compare_digit_sums(number1, number2)
print(result)