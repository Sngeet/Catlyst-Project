#ol(

#w=20
#if w<0 :
#    print("it is a +ve number")


#------------------------------------
#w=20
#if w<0 :
#    print("it is a +ve number")
#else:
#    print("it is a -ve number")

#c=int(input("enter ur number : "))
#if(c>0) :
#   print(c, "is a +ve number")
#elif(c==0):
#    print(c, "is a 0")
#else:
#   print(c, "is a -ve number")

#------------------------------------------------------------
# x=int(input("enter 1st number : "))
# y=int(input("enter 2nd number : "))
# z=int(input("enter 3rd number : "))
# if(x>y):
#    if(x>z):
#        print(x, "is  greater number")
#    else:
#        print(z, "is  greater number")
# else:
#    if(z>x):
#        print(z, "is  greater number")
#    else:
#        print(x, "is  greater number")


#1) check a number if -ve +ve ,0
#check number is even ,0dd
#check a pers0n is eigibIe t0 v0te
#find Iarger in 2 numbers
#find sma in 3 numbers
#t0 check number is divisibe by b0th 3,5

#1)
#z=int(input("enter 1st number : "))
#if(z<0):
##   print(z, "is a -ve number")
#elif(z==0):
 #   print(z, "is a 0")
#else:
  #  print(z, "is a +ve number")

#2)
#a=int(input("enter 1st number : "))
#if(a%2==0):
#    print(a, "is a even number")
#else:
 #   print(a, "is a 0dd number")

#3)

# age=int(input("enter age : "))
# if(age<18):
#    print("not eligble")
# else:
#    print("eligble")

#4)
#x=int(input("enter 1st number : "))
#y=int(input("enter 2nd number : "))
#if(x<y):
#    print(y, "is  greater number")
#else:
#    print(x, "is  greater number")


#5)
# x=int(input("enter 1st number : "))
# y=int(input("enter 2nd number : "))
# z=int(input("enter 3rd number : "))
# if(x<y):
#    if(x<z):
#        print(x, "is  small number")
#    else:
#        print(z, "is  small number")
# else:
#    if(z<y):
#        print(z, "is  small number")
#    else:
#         print(y, "is  small number")
    

#6)
# x=int(input("enter a number : "))
# if(x % 3==0 and x%5==0):
#    print(x, "divisibe by both")

# else:
#    print(x, " nt divisibe by both")


#7)
# x=float(input("enter ur Mark : "))
# if(x>=90):
#    print("A+")
# elif x>=80:
#    print("A")
# elif x>=70:
#    print("B+")    
# elif x>=60:
#    print("B")
# elif x>=50:
#    print("C+")
# elif x>=40:
#    print("C")
# elif x>=30  :
#    print("D+")
# else : 
#    print("F")



#__________________________________
units = int(input("Enter electricity units used: "))

if units <= 100:
   bill = units * 5

elif units <= 200:
   bill = (100 * 5) + ((units - 100) * 7)

elif units <= 300:
   bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

else:
   bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 20)

print("Total Electricity Bill = ", bill)






