# hiding the implementation deatils of a class and only showing the essential features to the users
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()