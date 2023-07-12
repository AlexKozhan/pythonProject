# from tkinter import *
# root=Tk()
# f1=Frame()
# f2=Frame()
# f3=Frame()
# f4=LabelFrame()
# b1=Button(f1, text="Добавить студента: ", font=15)
# b2=Button(f2, text="Добавить оценку: ", font=10)
# e1=Entry(f1, relief=SOLID, font=5)
# l2=Label(f4, width=40, font=15)
# l3=Label(f4, width=40, font=15)
# l4=Label(f4, width=40, font=15)
# b3=Button(f4, text="Добавить оценку: ", width=20, font=15)
# b4=Button(f4, text="Закрыть: ", width=20, font=15)
# e2=Entry(f4, relief=SOLID, font=15)
# lbx1=Listbox(f1, height=10, width=20, font="Arial 15", selectmode=EXTENDED)
# student_obj=list()
# class Student:
#     def __init__(self, fio):
#         self.fio=fio
#         self.marks=list()
#         def getFio(self):
#             return self.fio
#         def setFio(self, fio):
#             set.fio=fio
#         def getMarks(self):
#             return self.marks
#         def setMarks(self, marks):
#             set.marks=marks
#         def Add_mark(self, mark):
#             self.marks.append(mark)
#         def __str__(self):
#             return f"{self.fio} {', '.join(student_obj)}"
# def b1Funk(event):
#     student_obj.append(Student(e1.get()))
#     lbx1.insert(END, e1.get())
#     e1.delete(0,END)
# def b2Funk(event):
#     for i in student_obj:
#         if i.getFio()==lbx1.get(lbx1.curselection()):
#             f4.pack(side=LEFT,fill=Y)
#             l2['text']=f"Имя: \n{i.getFio()}"
#             l3['text'] = f"Оценки: \n{''.join(i.getMarks())}"
#             b3.pack()
#             e2.pack()
# def b3Funk(event):
#     for i in student_obj:
#         if i.getFio()==lbx1.get(lbx1.curselection()):
#             i.Add_mark(e2.get()+ ",")
#             e2.delete(0,END)
#             i.Add_mark(e2.get)
#             l3['text']=f"Оценки: \n{''.join(i.getMarks())}"
# def b4Funk(event):
#     f4.pack_forget()
#     l2['text']=''
#     l3['text']=''
# f1.pack(side=LEFT)
# f2.pack(side=LEFT)
# f3.pack(side=LEFT)
# e1.pack()
# b1.bind("<Button-1>", b1Funk)
# b1.pack()
# b2.bind("<Button-1>", b2Funk)
# b2.pack()
# lbx1.pack()
# b4.pack(anchor=NE)
# l2.pack()
# l3.pack()
# b4.bind("<Button-1>", b4Funk)
# b3.bind("<Button-1>", b3Funk)
# l4.pack()
# b2.pack()
# root.mainloop()
from tkinter import *

root = Tk()
root.title("Список студентов")

class Journal:
    def __init__(self):
        f1 = Frame()
        f2 = Frame()
        f1.pack(side=LEFT)
        f2.pack(side=LEFT)
        self.e = Entry(f1, width=20, font=("Arial", 27))
        self.lbox_stud = Listbox(f1, font=("Arial", 27))
        self.loadList_stud()
        self.e.pack()
        self.lbox_stud.pack()
        b1 = Button(f2, text="Добавить студента", font=("Arial", 27), command=self.addStudent)
        b2 = Button(f2, text="Добавить оценку", font=("Arial", 27), command=self.addPrize)
        b1.pack()
        b2.pack()
        self.group_stud = []

    def loadList_stud(self):
        with open("list_stud.txt", "r") as f:
            var = f.read().split("\n")
            var.sort()
            self.lbox_stud.delete(0, END)
            for i in var:
                if i != "":
                    self.lbox_stud.insert(END, i)

    def addStudent(self):
        if self.e.get() != "":
            with open(self.e.get() + ".txt", 'w') as file:
                file.write("")
            with open("list_stud.txt", "w") as f:
                f.write("\n" + self.e.get())
            self.e.delete(0, END)
            self.loadList_stud()

    def getStudent(self):
        with open(self.filename(), 'r') as file:
            self.var = file.read()
        return self.var

    def filename(self):
        return self.lbox_stud.get(self.lbox_stud.curselection()[0]) + ".txt"

    def addPrize(self):
        root1 = Tk()
        root1.title(f"Добавление оценок")
        # lbl = Label(root1, text=self.fln(), width=20, font=("Arial", 27))
        lbl = Label(root1, text=self.filename()[:-4], width=20, font=("Arial", 27))
        inf_text = Text(root1, height=10, width=20, font=("Arial", 27))
        inf_text.insert(1.0, self.getStudent())
        e1 = Entry(root1, width=7, font=("Arial", 27))
        b = Button(root1, text="Добавить оценку", font=("Arial", 27))
        lbl.pack()
        inf_text.pack()
        e1.pack()
        b.pack()

        def prize(event):
            if e1.get() != "":
                with open(self.filename(), 'a') as file:
                    for i in e1.get().split():
                        file.write(i + " ")
                e1.delete(0, END)
                inf_text.delete(1.0, END)
                inf_text.insert(1.0, self.getStudent())

        b.bind("<Button-1>", prize)
        root1.mainloop()


a = Journal()
root.mainloop()