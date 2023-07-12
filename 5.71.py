a = 1000
profit=0
s=0
for i in range (1, 11):
    s=float(a*2/100)
    profit+=s
    print("прибыль за ", i, " месяц составила", profit)
print (profit)


deposit = 1000
growth_rate = 0.02
month = int(input("Введите номер месяца (от 3 до 10): "))
if month < 3 or month > 10:
    print("Номер месяца должен быть от 3 до 10.")
else:
    for i in range(3, month + 1):
        growth = deposit * growth_rate
        deposit += growth
    print("Прирост суммы вклада за", month, "месяц:", growth)