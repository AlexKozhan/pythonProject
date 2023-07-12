from tkinter import *
root = Tk()
root.title("Студенты двоишники")
spisok=list()
f1=Frame()
f2=Frame()
e1=Entry(f2,width=20, font=("Arial", 15))
e2=Entry(f2,width=20, font=("Arial", 15))
b1=Button(f2,text='Добавить', width=20, font=("Arial", 15))
lbx=Listbox(f1, width=34, height=20, font=15)
class Student:
    def __init__(self, fio, age):
        self.fio = fio
        self.age = age
    def getFio(self):
        return self.fio
    def setFio(self, fio):
        self.fio = fio
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    def __str__(self):
        return f"{self.fio} {self.age}"
def knopka(event):
    spisok.append(Student(e1.get(), e2.get()))
    file= open("students/" + e1.get() + ".txt", 'w+')
    file.write(f"{e1.get()}\n")
    file.write(f"{e2.get()}")
    lbx.insert(END,f"{e1.get()} {e2.get()}")
    e1.delete(0,END)
    e2.delete(0,END)
f1.pack(side=LEFT)
f2.pack(side=LEFT)
e1.pack()
e2.pack()
lbx.pack(side=LEFT)
b1.bind("<Button-1>", knopka)
b1.pack()
root.mainloop()



