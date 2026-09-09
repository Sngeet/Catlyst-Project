# square= lambda x: x*x
# print(square(5))


a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
large= lambda a,b: a if a > b else b
print("largest",large(a,b))

a=int(input("enter the first number :"))
even= lambda x: x % 2 == 0
print(even(a))