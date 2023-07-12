import mysql.connector
from tkinter import *

root = Tk()
root.title("Список студентов")

# Подключение к базе данных MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="VFx33gA51542212",
    database="univer"
)

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
            # Добавление студента в базу данных
            cursor = mydb.cursor()
            sql = "INSERT INTO students (name) VALUES (%s)"
            val = (self.e.get(),)
            cursor.execute(sql, val)
            mydb.commit()

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

                # Добавление оценки в базу данных
                cursor = mydb.cursor()
                sql = "INSERT INTO grades (student_id, grade) VALUES (%s, %s)"
                val = (self.get_student_id(), e1.get())
                cursor.execute(sql, val)
                mydb.commit()

                e1.delete(0, END)
                inf_text.delete(1.0, END)
                inf_text.insert(1.0, self.getStudent())

        b.bind("<Button-1>", prize)
        root1.mainloop()

    def get_student_id(self):
        # Получение идентификатора студента из базы данных
        cursor = mydb.cursor()
        sql = "SELECT id FROM students WHERE name = %s"
        val = (self.lbox_stud.get(self.lbox_stud.curselection()[0]),)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None


a = Journal()
root.mainloop()
