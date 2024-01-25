class Car:
    # class or static variables
    wheels = 4

    def __init__(self):
        # instance variables
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c2.wheels = 10
Car.wheels = 5

print(c1.mil, c1.com, c1.wheels)
print(c2.wheels)

