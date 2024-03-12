class Student:
    def __init__(self,name,maths_score,science_score,english_score):
        self.name=name
        self.maths=maths_score
        self.science=science_score
        self.english=english_score

    def avg(self):
        total_score=self.maths+self.science+self.english
        avg_s=total_score/3
        return avg_s

    def cal_grade(self):
        avg_s=self.avg()
        if avg_s>90:
            print("A")
        elif 80 < avg_s <90:
            print("B")
        elif 70 < avg_s <80:
            print("C")
        elif 60 < avg_s <70:
            print("D")
        else:
            print("Fail")

student1=Student("athul",86,92,44)
avg_s=student1.avg()
grade=student1.cal_grade()
print("student:",student1.name)
print("Avarage score:",avg_s)

