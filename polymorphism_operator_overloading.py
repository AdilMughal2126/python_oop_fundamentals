class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m2
        m2 = self.m2 + other.m2
        st3 = Student(m1, m2)
        return st3

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(10, 20)
s2 = Student(50, 50)

s3 = s1 + s2
print(s1)
print(s2)
print(s3)
