# There are 4 ways of implementing polymorphism
# Duck Typing
# Operator Overloading
# Method Overloading
# Method Overriding

# Duck Typing comes from a phrase "If it looks like a duck, walks like a duck, swims likes a duck and
# quack like a duck than it is probably a duck"

class PyCharm:
    def execute(self):
        print("Compiling.")
        print("Running.")


class MyEditor:
    def execute(self):
        print("Compiling.")
        print("Spell check")
        print("Convention check")
        print("Running.")


class Laptop:
    def code(self, ide):
        ide.execute()


lap1 = Laptop()
editor = PyCharm()
lap1.code(editor)

lap2 = Laptop()
my_editor = MyEditor()
lap2.code(my_editor)


