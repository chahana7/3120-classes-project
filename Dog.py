from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) 
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def move(self):
        return "The dog runs around happily."

    def fetch(self):
        return f"{self.name} fetches the ball with excitement!"
