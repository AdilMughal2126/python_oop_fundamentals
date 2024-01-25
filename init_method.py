class Computer:
    # it is like a constructor if you are from Java or C++ background
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


com1 = Computer("Rayzen i5", "16gb")
com2 = Computer("i7", "16gb")
com1.config()
com2.config()
