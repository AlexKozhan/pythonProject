from tkinter import *
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Journal:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:VFx33gA51542212@localhost/newDB')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.root = Tk()
        self.root.title("Список студентов")

        self.f1 = Frame()
        self.f2 = Frame()
        self.f1.pack(side=LEFT)
        self.f2.pack(side=LEFT)
        self.e = Entry(self.f1, width=20, font=("Arial", 27))
        self.lbox_stud = Listbox(self.f1, font=("Arial", 27))
        self.loadList_stud()
        self.e.pack()
        self.lbox_stud.pack()
        b1 = Button(self.f2, text="Добавить студента", font=("Arial", 27), command=self.addStudent)
        b2 = Button(self.f2, text="Добавить оценку", font=("Arial", 27), command=self.addPrize)
        b1.pack()
        b2.pack()
        self.group_stud = []

    def loadList_stud(self):
        students = self.session.query(Student).order_by(Student.name).all()
        self.lbox_stud.delete(0, END)
        for student in students:
            self.lbox_stud.insert(END, student.name)

    def addStudent(self):
        if self.e.get() != "":
            student = Student(name=self.e.get())
            self.session.add(student)
            self.session.commit()
            self.e.delete(0, END)
            self.loadList_stud()

    def getStudent(self):
        student = self.session.query(Student).filter_by(name=self.filename()[:-4]).first()
        return student

    def filename(self):
        return self.lbox_stud.get(self.lbox_stud.curselection()[0]) + ".txt"

    def addPrize(self):
        root1 = Tk()
        root1.title(f"Добавление оценок")
        lbl = Label(root1, text=self.filename()[:-4], width=20, font=("Arial", 27))
        inf_text = Text(root1, height=10, width=20, font=("Arial", 27))
        student = self.getStudent()
        if student:
            inf_text.insert(1.0, student.name)
        e1 = Entry(root1, width=7, font=("Arial", 27))
        b = Button(root1, text="Добавить оценку", font=("Arial", 27))
        lbl.pack()
        inf_text.pack()
        e1.pack()
        b.pack()

        def prize(event):
            if e1.get() != "":
                if student:
                    student.name += " " + e1.get()
                else:
                    student = Student(name=e1.get())
                    self.session.add(student)
                self.session.commit()
                e1.delete(0, END)
                inf_text.delete(1.0, END)
                student = self.getStudent()
                if student:
                    inf_text.insert(1.0, student.name)

        b.bind("<Button-1>", prize)
        root1.mainloop()


if __name__ == '__main__':
    a = Journal()
    a.root.mainloop()
