import tkinter as tk

def calculate():
    num1 = entry1.get()
    num2 = entry2.get()
    operator = operation.get()

    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "ошибка: деление на ноль"
        else:
            result = "ошибка: неверная операция"
    else:
        result = "ошибка: введите числа"

    result_label.config(text=str(result))

# Создание графического интерфейса
root = tk.Tk()
root.title("Калькулятор")

# Поля ввода чисел
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Выбор операции
operation = tk.StringVar()
operation.set('+')

operation_frame = tk.Frame(root)
operation_frame.pack()

add_button = tk.Radiobutton(operation_frame, text="+", variable=operation, value='+')
add_button.pack(side=tk.LEFT)

subtract_button = tk.Radiobutton(operation_frame, text="-", variable=operation, value='-')
subtract_button.pack(side=tk.LEFT)

multiply_button = tk.Radiobutton(operation_frame, text="*", variable=operation, value='*')
multiply_button.pack(side=tk.LEFT)

divide_button = tk.Radiobutton(operation_frame, text="/", variable=operation, value='/')
divide_button.pack(side=tk.LEFT)

# Кнопка "Вычислить"
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

# Метка для вывода результата
result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла обработки событий
root.mainloop()