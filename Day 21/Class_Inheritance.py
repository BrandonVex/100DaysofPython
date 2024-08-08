class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        # super() is used to call the parent class constructor which is the __init__ method in this case from the Animal class
        super().__init__()

    def breathe(self):
        # the super() function is used to call the parent class method breathe() from the Animal class
        # this prints "Inhale, exhale."
        super().breathe()
        # this prints "doing this underwater."
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
