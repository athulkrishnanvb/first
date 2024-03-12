class School:
    def open(self):
        print("opening")

class Student(School):
    def std(self):
        print("Ok")

obj=Student()
obj.open()
obj.std()
