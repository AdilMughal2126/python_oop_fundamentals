class Computer:
    def __init__(self):
        self.name = "Adil"
        self.age = 23

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.name = "John"

print(c1.name)
print(c2.name)

# Every object is store on a heap to get the id on the heap use this method, In python every datatype is an object int,
# float, double etc.
# everytime you create an object it is allocated new space

print(id(c1))

print(c1.compare(c2))
