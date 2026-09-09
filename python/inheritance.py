# 1.Single Inheritance:
# class animal:
#     def eat(self):
#         print("eating")
# class Dog(animal):
#     pass
# new=Dog()
# new.eat() 

# class animal:
#      def eat(self):
#          print("eating")
# class Dog(animal):
#      def bark(self):
#         print("barking")
# new=animal()
# new.bark()

 # 2. Multiple Inheritances:
# class catalsyt:
#     def institute(self):
#         print("admission")

# class python:
#     def fullstack(self):
#         print("class started")
# class student(catalsyt,python):
#     pass
# hashim=student()
# hashim.institute()
# hashim.fullstack()
 
# 3.Multilevel Inheritance:
# class Animal:
#     def sound(self):
#         print("make sound")
# class Mammal(Animal):
#     def milk(self):
#         print("milk providing")
# class dog(Mammal):
#     def bark(self):
#         print("barking")
# obj1=dog()
# obj1.sound()
# obj1.milk()
# obj2=Mammal()
# obj2.sound()

# 4.Hierarchical Inheritance:
# class Animal:
#     def body(self):
#         print("Animals are cute")
# class Dog(Animal):
#     def sound(Animal):
#         print("bow bow")
# class cat(Animal):
#     def milk(Animal):
#         print("meow meow")
# obj1=Dog()
# obj1.sound()
# obj2=cat()
# obj2.milk()
# 5.Hybrid Inheritance:
# class A:
#     def showA(self):
#         print("Class A")
# class B(A):
#     def showB(self):
#         print("Class B")
# class C(A):
#     def showC(self):
#         print("Class C")
# class D(B, C):
#     def showD(self):
#         print("Class D")
# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()

# Methodoverriden 
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)

D = Dog("Buddy", "Labrador")
print(D.name, D.breed)