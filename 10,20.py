def get_digit_sum(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number //= 10

    return digit_sum

def get_lucky_numbers():
    lucky_numbers = []

    for number in range(100000, 1000000):
        first_three_digits = number // 1000
        last_three_digits = number % 1000

        if get_digit_sum(first_three_digits) == get_digit_sum(last_three_digits):
            lucky_numbers.append(number)

    return lucky_numbers

# Пример использования
lucky_numbers = get_lucky_numbers()
print("Шестизначные счастливые номера:")
print(lucky_numbers)