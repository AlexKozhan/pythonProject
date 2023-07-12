#spisok = list(range(20))
#for i in spisok:
   # if i%10==7:
        #print (i)

a = 1  # Начальное число последовательности
position = 0  # Порядковый номер первого числа оканчивающегося на 7
for i in range(1, 21):
    if a % 10 == 7:
        position = i
        break
    a = a * a
if position != 0:
    print(f"Число, оканчивающееся на 7, найдено на позиции {position}")
else:
    print("В последовательности нет чисел, оканчивающихся на 7")