class Student:
    def __init__(self, name):
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print(self.name)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.com = "Hp"
            self.ram = "16 gb"

        def show(self):
            print(self.com, self.ram)


s1 = Student("Adil")
s1.show()

laptop = Student.Laptop()
laptop.show()

