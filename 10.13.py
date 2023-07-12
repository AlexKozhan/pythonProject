def count_perfect_squares(n, sequence):
    count = 0

    for num in sequence:
        if is_perfect_square(num):
            count += 1

    return count

def is_perfect_square(num):
    if num < 0:
        return False

    root = int(num ** 0.5)
    return root * root == num

# Пример использования
n = 6
sequence = [1, 2, 3, 4, 5, 6]

perfect_square_count = count_perfect_squares(n, sequence)
print("Количество полных квадратов: ", perfect_square_count)