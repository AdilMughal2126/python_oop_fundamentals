# If you create an object of a sub class it will first try to find the constructor of sub class
# if it is not found it will call constructor of super class
# How constructor behaves in inheritance
# How to use super() in inheritance
# Method Resolution Method (MRO)

class A:
    def __init__(self):
        print("A init")

    def feature1(self):
        print("Feature 1 in A is working.")

    def feature2(self):
        print("Feature 2 is working.")


class B:
    def __init__(self):
        print("A init")

    def feature1(self):
        print("Feature 1 is working.")

    def feature4(self):
        print("Feature 4 is working.")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")


a1 = C()
a1.feature1()
