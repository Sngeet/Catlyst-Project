# Oops practical questions:-

# 1.Bank Account
# Create a BankAccount class.
# Add deposit() and withdraw() methods.
# Prevent withdrawal if balance is insufficient.
# Display account details.


# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print("deposited:",amount)
#     def withdrew(self,amount):
#         if amount <=self.balance:
#             self.balance-=amount
#         else:
#             print("Insufficient balance")
#     def display(self):
#             print(self.name,self.balance)
# a=BankAccount("aseem",5000)
# a.deposit(1000)
# a.withdrew(2000)
# a.display()


# 2.Student Management
# Create a Student class.
# Store name, roll number and marks.
# 3.Create a method to calculate percentage and grade.


# class student:
#      def __init__(self,name,roll,marks):
#           self.name=name
#           self.roll=roll
#           self.marks=marks
#      def percentage(self):
#          return sum(self.marks)
#      def grade(self):
#          p=self.percentage()
#          if p>=90:
#            return "A"
#          elif p>=75:
#              return "B"
#          elif p>=50:
#              return "C"
#          else:
#              return "D"
# s=student("Ace",10,[80,70,90]) 
# print(s.name)
# print(s.percentage())
# print(s.grade())
 
# 4.Create an Employee class.
# Store name, ID and salary.
# Create a method to calculate annual salary.


# class Employee:
#     def __init__(self, name, id, salary):
#         self.name = name
#        self.id = id
#         self.salary = salary
#     def annual_salary(self):
#         return self.salary * 12
# e = Employee("Aseem", 101, 20000)
# print(e.name)
# print(e.annual_salary())


# 5.Create a Car class.
# Add start(), stop() and display_info() methods.
# Create multiple car objects.


# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
#     def display_info(self):
#         print("Brand:", self.brand)
# c1 = Car("Toyota")
# c2 = Car("Maruti")
# c1.display_info()
# c1.start()
# c2.display_info()
# c2.start() 
# 6.Create a Product class with name, price and quantity.
# Create a method to calculate total price.
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total(self):
#         return self.price * self.quantity
# p = Product("Pen", 20, 5)
# print(p.total())


# 7.Create Product and ShoppingCart classes.
# Add products to the cart.
# Remove products.
# Calculate the total bill.


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class ShoppingCart:
#     def __init__(self):
#         self.products = []
#     def add(self, product):
#         self.products.append(product)
#     def total(self):
#         total = 0
#         for p in self.products:
#             total = total + p.price
#         return total
# p1 = Product("Pen", 20)
# p2 = Product("Book", 100)
# cart = ShoppingCart()
# cart.add(p1)
# cart.add(p2)
# print(cart.total())


# # 8.Create Book and Library classes.
# # Add books.
# # Borrow a book.
# # Return a book.
# # Prevent borrowing an already borrowed book.


# class Book:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed = False
# class Library:
#     def borrow(self, book):
#         if book.borrowed:
#             print("Already borrowed")
#         else:
#             book.borrowed = True
#             print("Book borrowed")
#     def return_book(self, book):
#         book.borrowed = False
#         print("Book returned")
# b = Book("Python")
# library = Library()
# library.borrow(b)
# library.borrow(b)
# library.return_book(b)


# # 9.Create an Account class.
# # Create an ATM class.
# # Use methods for PIN verification, withdrawal, deposit and balance checking.


# class Account:
#     def __init__(self, pin, balance):
#         self.pin = pin
#         self.balance = balance
# class ATM:
#     def check_pin(self, account, pin):
#         return account.pin == pin
#     def deposit(self, account, amount):
#         account.balance += amount
#     def withdraw(self, account, amount):
#         if amount <= account.balance:
#             account.balance -= amount
#         else:
#             print("Insufficient balance")
#     def balance(self, account):
#         print("Balance:", account.balance)
# a = Account(1234, 5000)
# atm = ATM()

# if atm.check_pin(a, 1234):
#     atm.deposit(a, 1000)
#     atm.withdraw(a, 2000)
#     atm.balance(a)
# else:
#     print("Wrong PIN")


# # 10.Create a parent Employee class.
# # Create child classes Developer and Manager.
# # Give each child class its own work() method.
# # Demonstrate method overriding.


# class Employee:
#     def work(self):
#         print("Employee working")
# class Developer(Employee):
#     def work(self):
#         print("Developer coding")
# class Manager(Employee):
#     def work(self):
#         print("Manager managing")
# d = Developer()
# m = Manager()
# d.work()
# m.work()


# 11.Create a parent Vehicle class.
# Create Car, Bike and Bus classes.
# Use inheritance.
# Override a start() method in each child class.


# class Vehicle:
#     def start(self):
#         print("Vehicle starts")
# class Car(Vehicle):
#     def start(self):
#         print("Car starts")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts")
# class Bus(Vehicle):
#     def start(self):
#         print("Bus starts")
# Car().start()
# Bike().start()
# Bus().start()


# 12.Create an abstract Payment class.
# Create CreditCardPayment, UPIPayment and CashPayment.
# Each class should implement pay() differently.
# Demonstrate abstraction + polymorphism.


# class Card(Payment):
#     def pay(self):
#         print("Paid by Card")
# class UPI(Payment):
#     def pay(self):
#         print("Paid by UPI")
# class Cash(Payment):
#     def pay(self):
#         print("Paid by Cash")
# Card().pay()
# UPI().pay()
# Cash().pay()


# 13.Create an Employee parent class.
# Create Developer and Manager.
# Override calculate_salary() in each class.
# Demonstrate inheritance + polymorphism.


# class Employee:
#     def salary(self):
#         print("Employee salary")
# class Developer(Employee):
#     def salary(self):
#         print("Developer salary = 50000")
# class Manager(Employee):
#     def salary(self):
#         print("Manager salary = 70000")
# employees = [Developer(), Manager()]
# for e in employees:
#     e.salary()


# 14.Create Person as a parent class.
# Create Doctor and Patient as child classes.
# Add suitable methods and attributes.
# Demonstrate inheritance.


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Name:", self.name)
# class Doctor(Person):
#     def treat(self):
#         print("Doctor treats patient")
# class Patient(Person):
#     def take_medicine(self):
#         print("Patient takes medicine")
# d = Doctor("John")
# p = Patient("Rahul")
# d.display()
# d.treat()
# p.display()
# p.take_medicine()


# 15.Create FoodItem, Order and Customer classes.
# Add food items to an order.
# Calculate the total.
# Apply different discounts using polymorphism.


# class FoodItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Order:
#     def __init__(self):
#         self.items = []
#     def add(self, item):
#         self.items.append(item)
#     def total(self):
#         total = 0
#         for item in self.items:
#             total += item.price
#         return total
# class Customer:
#     def discount(self, amount):
#         return amount
# class Regular(Customer):
#     def discount(self, amount):
#         return amount * 0.9
# class Premium(Customer):
#     def discount(self, amount):
#         return amount * 0.8
# f1 = FoodItem("Pizza", 300)
# f2 = FoodItem("Burger", 200)
# order = Order()
# order.add(f1)
# order.add(f2)
# total = order.total()
# customer = Premium()
# print("Total:", total)
# print("Final:", customer.discount(total))


# 16.Create a base Product class.
# Create Electronics, Clothing and Book classes.
# Each should calculate its final price differently.
# Use inheritance, encapsulation and polymorphism.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    def price(self):
        return self.__price
class Electronics(Product):
    def price(self):
        return super().price() + 1000
class Clothing(Product):
    def price(self):
        return super().price() - 200
class Book(Product):
    def price(self):
        return super().price() - 100
e = Electronics("Laptop", 50000)
c = Clothing("Shirt", 2000)
b = Book("Python Book", 1000)
print(e.price())
print(c.price())
print(b.price())