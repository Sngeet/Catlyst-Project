# 1V)

#1) student managemet creatre a student class store name roll no mark
#2) write a code f closure
#3) take 2 list find common elements 
# 
#  

#3) 
# l1=[1,2,3,4,5,6,7]
# l2=[4,5,6,7,8,9]
# for i in l1:
#     if i in l2:
#         print(i)
       


#2)
# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
# add=outer(10)
# print(add(6))

#1)

class Student:
    def __init__(self, name, roll_no,mark):
        self.name = name
        self.no = roll_no
        self.mark = mark
s1 =Student("Sangeeth" , 21 , 89)
print(s1.name)
print(s1.no)
print(s1.mark)