# Pillers of oops
#1.class
#2.object
#3.encapsulation
#4.inheritance
#5.abstraction
#6.polymorphism


# class Student:
#     pass
# s1=Student()
# s2=Student()
# print(s2)
# print(s1)

# class student:
#     def introduce(self):
#         print("hello I am Student")
# s=student()
# s.introduce()
  
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
first=Student("devu",23)
print(first.name)
print(first.age)