#1) multiple parameter arguments:

# def new(a,b):
#     print(a+b)
# new(3,4)

#2)  default parameter

# def greet(name="sangeeth",message="welcome"):
#     print(message,name)
# greet()   
# #greet("alice")
# greet("sangeeth", "good morning")
# greet()

#3) KeyWord Argument 

# def student(name,age):
#     print(name,age)
# student(age=21,name="rahul")

#4)positional argument  // how we enter the values in arguments thats how parameter vales are assigned

# def greet(name,message):
#      print(message,name)
 
# greet("alice","welcome")
# greet("welcome","alice")  


#arbitary argument

def san(*arg): #arbitary keyword argument
     print(arg)
san(1,2,3)


# #arbitary keyword argument

def san(**kwarg): 
     print(kwarg)
san(a=1,b=3,c=5)
