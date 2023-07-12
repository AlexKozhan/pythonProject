def find_prime_numbers():
    prime_numbers = []

    for num in range(100, 1000):
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
nb
    return True

# Пример использования
prime_numbers = find_prime_numbers()
print("Трехзначные простые числа:")
print(prime_numbers)