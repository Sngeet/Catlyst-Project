# l=[]
# l.append(10) #single element
# print(l)
# l.append([20,30]) #create a list inside a list
# print(l)
# l.append([20,30,40])
# print(l)
# print(l[0])
# print(l[1][1])
# l.extend([22,34,44]) #insert multiple elements
# print(l)

# s = input("Enter a string: ")

# for ch in set(s):
#     print(ch, ":", s.count(ch))

# s = int(input("Enter no.of list : "))
# arr=[]
# for i in range(s):
#     a=int(input("enter the numbers : "))
#     arr.append(a)
# print(arr)
# result = []
# for x in arr:
#     if x not in result:
#         result.append(x)

# print(result)

# s = input("Enter a sentence: ")

# words = s.split()

# print("Number of words:", len(words))

# s = input("Enter a sentence: ")

# print(s.title())

# s = input("Enter a string: ")

# for ch in s:
#     if s.count(ch) == 1:
#         print("First non-repeating character:", ch)
#         break
# else:
#     print("No non-repeating character found")
    

# s = input("Enter a string: ")

# for ch in set(s):
#     print(ch, ":", s.count(ch))


s1={11,22,33,44,54}
s2={11,22,33,44,33,54,55,66,77}

print(s2.issuperset(s1)) #all elements in s1 are present in s2 
print(s1.issubset(s2))