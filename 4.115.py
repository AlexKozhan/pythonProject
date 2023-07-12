n = int(input('Введите год нашей эры - '))
if abs(n-1984)%12 == 0:
    print ('Крыса', end = ', ')
elif abs(n-1984)%12 == 1:
    print('Корова', end = ', ')
elif abs(n-1984)%12 == 2:
    print('Тигр', end = ', ')
elif abs(n-1984)%12 == 3:
    print('Заяц', end = ', ')
elif abs(n-1984)%12 == 4:
    print('Дракон', end = ', ')
elif abs(n-1984)%12 == 5:
    print('Змея', end = ', ')
elif abs(n-1984)%12 == 6:
    print('Лошадь', end = ', ')
elif abs(n-1984)%12 == 7:
    print('Овца', end = ', ')
elif abs(n-1984)%12 == 8:
    print('Обезьяна', end = ', ')
elif abs(n-1984)%12 == 9:
    print('Петух', end = ', ')
elif abs(n-1984)%12 == 10:
    print('Собака', end = ', ')
elif abs(n-1984)%12 == 11:
    print('Свинья', end = ', ')
if ((n+6)%10+2)/2<2:
    print ('Зеленый')
elif 2<=((n+6)%10+2)/2<3:
    print('Красный')
elif 3<= ((n + 6) % 10 + 2) / 2 < 4:
    print('Желтый')
elif 4 <= ((n + 6) % 10 + 2) / 2 < 5:
    print('Белый')
elif 5 <= ((n + 6) % 10 + 2) / 2 < 6:
    print('Черный')
