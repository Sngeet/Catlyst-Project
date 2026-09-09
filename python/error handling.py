try:
    result=10/0
except ZeroDivisionError:
    print("zerodivision error")  
else:
    print("result")   
finally:
    print("code completed")       

try:
    l=[23,45,6]
    l.add(23)
except AttributeError:
    print("in this datatype doesn't belong to this attr:")
else:
    print(l)
finally:
    print("code completed")      



#key error
 
student = {
    "name": "Riya",
    "age": 21,
    "course": "Python"
}

key = input("Enter key: ")

try:
    print("Value:", student[key])
except KeyError:
    print("This key does not exist.") 
else:
    print("result")    
finally:
    print("code completed") 

#index error

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index is out of range.")
else:
    print("result")

finally:
    print("code completed")