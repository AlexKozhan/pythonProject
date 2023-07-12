print ('Для выхода нажмите Y')
while True:
    data = input('введите сумму для обмена: ')
    if data.lower() == 'y':
        break
    money = int(data)
    if money < 0
        print ("Сумма должна быть положительной")
        continue
    cache = round (money / 56, 2)
    print ('К выдаче', cache, 'долларов')
print ('Работа обменного пункта завершена')