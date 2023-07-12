class Car:
    def __init__(self, marka, model, color, price):
        self.marka=marka
        self.model=model
        self.color=color
        self.price=price
    def getMarka(self):
        return self.marka
    def setMarka(self, marka):
        self.marka=marka
    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def __str__(self):
        return f"{self.marka} {self.model} {self.color} {self.price}"
class Customer:
    def __init__(self, fio, age, money, sex):
        self.fio=fio
        self.age=age
        self.money=money
        self.sex=sex
    def getFio(self):
        return self.fio
    def setFio(self, fio):
        self.fio = fio
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    def getMoney(self):
        return self.money
    def setMoney(self, money):
        self.money = money
    def getSex(self):
        return self.sex
    def setSex(self, sex):
        self.sex = sex
    def __str__(self):
        return f"{self.fio} {self.age} {self.money} {self.sex}"
mers=Car("mersedes", "w140", "black", 10000)
audi=Car("audi", "a8", "white", 15000)
bmw=Car("bmw", "x5", "blue", 7000)

c1=Customer("bob", 45, 40000, "man")
c2=Customer("sam", 25, 10000, "man")
c3=Customer("jack", 15, 400, "man")

list_car=[mers, audi, bmw]
list_buyer=[c1, c2, c3]
for i in list_buyer:
    i.wish_color=input(f"{i.getFio()} ищет цвет: ")
    i.wish_price=int(input(f"{i.getFio()} ищет цену до: "))
    print (i.getFio())
    for j in list_car:
        if i.wish_color==Car.getColor(j) and i.wish_price>=Car.getPrice(j):
            print(j)