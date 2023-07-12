
import random

# Создание двумерного массива с случайными зарплатами
salary_array = [[random.randint(1000, 5000) for _ in range(12)] for _ in range(20)]

# Вывод двумерного массива на экран
for person_salary in salary_array:
    print(person_salary)

# Выбор человека и расчет общей зарплаты за год
person_index = int(input('Номер работника '))
person_salary = salary_array[person_index]
total_salary = sum(person_salary)

# Вывод общей зарплаты на экран
print("Общая зарплата за год для человека", person_index, ":", total_salary)