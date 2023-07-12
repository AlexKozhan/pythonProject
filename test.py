line='123dkskdk'
ints = []
try:
    for line in ints:
        ints.append(int(line))
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
    print('Всё хорошо.')
finally:
    print('Я закрыл файл.')
