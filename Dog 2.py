from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
		    self.age = age

    def make_sound(self):
        return f"{self.name} says Woof!"

    def move(self):
    		return return f"{self.name} moves."
