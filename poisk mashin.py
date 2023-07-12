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
#mers=car("mers", "w140", "black", 10000)
#print(mers.price)
#print(mers.__str__())
#print(mers)
#x=str(mers)
#print(x)
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
#car=[car("mersedes", "e212", "black", 40000), car("bmw", "x5", "black", 1000)]
# car=[]
# cus=[]
# for i in range(3):
#     marka=input("marka = ")
#     model = input("model = ")
#     color = input("color = ")
#     price = float(input("price = "))
#     ob=Car(marka, model, color, price)
#     car.append(ob)
# for i in range(3):
#     fio = input("sfio = ")
#     age = input("sage = ")
#     money = float(input("smoney = "))
#     sex = input("ssex = ")
#     ob=Customer(fio, age, money, sex)
#     cus.append(ob)
#for i in cus:
 #   print(i.getFio())
  #  for j in car:
  #      if i.getMoney()>=j.getPrice():
     #       print(j)
#Alex=customer("КАА", 23, 5000, "мужской")

from tkinter import *
root = Tk()
root.title ("Search for cars")
#root.geometry ("600x400")
car=[]
cus=[]
f=Frame(root)
f1=Frame(f)
l1=Label(f1, text="Marka ", width=30, font=("Arial", 14))
e1=Entry(f1, width=30, font=("Arial", 14))
l2=Label(f1, text="Model", width=30, font=("Arial", 14))
e2=Entry(f1, width=30, font=("Arial", 14))
l3=Label(f1, text="Color", width=30, font=("Arial", 14))
e3=Entry(f1, width=30, font=("Arial", 14))
l4=Label(f1, text="Price", width=30, font=("Arial", 14))
e4=Entry(f1, width=30, font=("Arial", 14))
b1=Button(f1, text="Add",font=("Arial", 14))
def b1f(event):
    marka=e1.get()
    model=e2.get()
    color=e3.get()
    price=float(e4.get())
    car.append(Car(marka, model, color, price))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
b1.bind("<Button-1>", b1f)
f2=Frame(f)
l21=Label(f2, text="FIO", width=30, font=("Arial", 14))
e21=Entry(f2, width=30, font=("Arial", 14))
l22=Label(f2, text="Age", width=30, font=("Arial", 14))
e22=Entry(f2, width=30, font=("Arial", 14))
l23=Label(f2, text="Money", width=30, font=("Arial", 14))
e23=Entry(f2, width=30, font=("Arial", 14))
l24=Label(f2, text="Sex", width=30, font=("Arial", 14))
e24=Entry(f2, width=30, font=("Arial", 14))
b21=Button(f2, text="Add",font=("Arial", 14))
def b21f(event):
    fio=e21.get()
    age=e22.get()
    money=float(e23.get())
    sex=e24.get()
    cus.append(Customer(fio, age, money, sex))
    e21.delete(0, END)
    e22.delete(0, END)
    e23.delete(0, END)
    e24.delete(0, END)
b21.bind("<Button-1>", b21f)
b31=Button(root, text="Result",font=("Arial", 14))
#l31=Label(root, width=30,font=("Arial", 14))
l31=Text(root, width=30, height=10, font=("Arial", 14))
def b31f(event):
    s=""
    for i in cus:
        s+=i.getFio()+":\n"
        for j in car:
            if i.getMoney()>=j.getPrice():
                s+=str(j)+"\n"
    #l31["text"]=s
    l31.insert(1.0,s)
b31.bind("<Button-1>", b31f)
f.pack()
f1.pack(side=LEFT)
f2.pack(side=LEFT)
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()
b1.pack()
l21.pack()
e21.pack()
l22.pack()
e22.pack()
l23.pack()
e23.pack()
l24.pack()
e24.pack()
b21.pack()
b31.pack()
l31.pack()
root.mainloop()






