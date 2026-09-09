# l=[]
# l.append(10) #single element
# print(l)
# l.append([20,30]) #create a list inside a list
# print(l)
# l.append([20,30,40])
# print(l)
# # print(l[0])
# # print(l[1][1])
# l.extend([22,34,44]) #insert multiple elements
# print(l)

# l.insert(2,56) #insert a element at any index
# print(l)

#l.clear  #to clear all list

# l.pop(4) #remove the element on 4th index 
# print(l)

# l.pop() #remove the element on last index
# print(l)

# l.remove(56)  # remove the element
# print(l)

l=[12,25,32,13,45,32,54,33]
c=l.count(32)
print((c))  #count the no how many time appeared

print(l.index(45))
# l.sort()    #for sort
# print(l)

# l.reverse()
# print(l)



'''my work '''

'''# l=int(input("enter a number of elemennts : "))
# arr=[]
# for i in range(l):
#     a=int(input("entet the numbers : "))
#     arr.append(a)
# print(arr)'''

'''example questions'''
l=[]
l.extend([22,34,44,44,66,66])
print(l)     #print element
print(l[0])  #print first element
print(l[4])  #print last element
print(max(l))
print(min(l))
print(len(l))

l.reverse()
print(l)

l=[22,34,44,44,66,66]
c=l.count(54)
print((c))

l.pop(5)
print(l)



l.insert(6,77)
print(l)

print()

for i in l:
    print(i,l.count(i))  #count each element

avg=sum(l) / len(l)
print(avg)

l=int(input("enter a number of elemennts : "))
arr=[]
for i in range(l):
    a=int(input("entet the numbers : "))
    arr.append(a)
print(arr)


