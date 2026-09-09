# from abc import ABC,abstractmethod        Abstraction in the python means hiding thhe complex details and showing only the essential parts
# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(ABC):
#     def sound(self):
#         return "Barks"
# class Cat:
#     def sound(self):
#         return "meow"

# dog=Dog()
# cat=Cat()
# print(dog.sound())
# print(cat.sound())

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        return "baleno"
car=Car()
print(car.start())