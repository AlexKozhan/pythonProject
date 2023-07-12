# студенты
from tkinter import *


root = Tk()
root.title("успеваемость")

class Student:
    def __init__(self, fio):
        self.fio = fio
        self.list_otm = []
    def __str__(self):
        return f"{self.fio} {self.list_otm}"
class Journal:
    def __init__(self):
        f1 = Frame()
        f2 = Frame()
        f1.pack(side=LEFT)
        f2.pack(side=LEFT)
        self.e = Entry(f1, width=20, font=("Arial", 27))
        self.list_stud = Listbox(f1, font=("Arial", 27))
        self.e.pack()
        self.list_stud.pack()
        b1 = Button(f2, text="Добавить студента", font=("Arial", 27), command=self.add_stud)
        b2 = Button(f2, text="Добавить оценку", font=("Arial", 27), command=self.add_prize)
        b1.pack()
        b2.pack()
        self.group_stud = []

    def add_stud(self):
        self.group_stud.append(Student(self.e.get()))
        self.list_stud.insert(END, self.e.get())
        self.e.delete(0, END)

    def add_prize(self):
        root1 = Tk()
        x0 = list(self.list_stud.curselection())
        root1.title(f"{x0}")
        x = Label(text=self.group_stud[x0].str(), width=20, font=("Arial", 27))
        y = Entry(width=20, font=("Arial", 27))
        x.pack()
        y.pack()
        b = Button(root1, text="Добавить оценку", font=("Arial", 27), command=self.prize)
        b.pack()

    def prize(self):
        pass
root.mainloop()