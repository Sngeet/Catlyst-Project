#remove in set remove the given element is present else show error
#discard it remove if it present else not not show any error msg like removed
#pop  remove element from anywhere in the set

#isdisjoint if commen element present print false

# s=set() # null set
# print(s)

# s.add(12)
# print(s)

# s.add((1,2,3)) #adding tuple into aset (only tuple can add into a set not list or another set)
# print(s)

# s.update({1,2,3,4}) #adding multiple values into a set
# print(s)

# s1={11,22,33,44,55,66}
# s2={12,23,34,45,33,55}

# print(s1.difference(s2)) #remove common elelment from first set
# print(s1.intersection(s2)) #print commen elements
# print(s1.isdisjoint(s2))  #print false  if  common elememts are present
# print(s1.union(s2))       #print all elements

s1={11,22,33,44,54}
s2={11,22,33,44,33,55,66,77}

# print(s2.issuperset(s1)) #all elements in s1 are present in s2 
# print(s1.issubset(s2))   #all elements in s1 are only from s2 

# print(s2.difference(s1))  
print(s2.symmetric_difference(s1))  
s2.difference_update(s1)
print(s2)

'''practice questions'''
#1)

a=set()
a.update({1,2,3,4,5})
print(a)

#2)
a.add(6)
print(a)

#3)
a.remove(4)
print(a)

#4)
b=int(input("enter the number to search: "))
for b in a:
    print("present")
    break
else:
    ("not present")

#5)
print(len(a))

#6)
a.clear()
print(a)

#7)
s1={2,4,6,8,9,7}
s2={3,5,7,9,6,4}
s3={1,2,3,4,5,6,7,8,9}

#8)
print(s1.union(s2))

#9)
print(s1.intersection(s2))

#10)
print(s1.issubset(s3))

#11)
print(s1.isdisjoint(s2))

#12)