# We have two types of methods
# Accessors -> to access values
# Mutators -> to modify state of object

class Student:
    school = "Unique Solutions School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a School class in abc module.")


s1 = Student(1, 2, 10)
print(s1.avg())
print(Student.get_school())
Student.info()
