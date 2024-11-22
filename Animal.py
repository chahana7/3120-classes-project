from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
git add Animal.py
git commit -m "Added abstract Animal class"
git push origin main
