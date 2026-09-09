'''String'''

'''#1) Replace all spaces with hyphens (-)

s = input("Enter a string: ")

print(s.replace(" ", "-"))

#2)Remove all spaces from a string

s = input("Enter a string: ")

print(s.replace(" ", ""))

#3)Check if two strings are anagrams

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#4)Find the frequency of each character in a string

s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))

#5)Remove duplicate characters from a string

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#6)Find the largest word in a sentence

s = input("Enter a sentence: ")

words = s.split()

largest = max(words, key=len)

print("Largest word:", largest)

#7)Count the number of words in a sentence

s = input("Enter a sentence: ")

words = s.split()

print("Number of words:", len(words))

#8)Capitalize the first letter of every word

s = input("Enter a sentence: ")

print(s.title())

#9)Find the first non-repeating character


s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")'''



   #list Practice 

'''#1)Create a list of 10 numbers and print each element using a loop

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in l:
    print(i)

#2)Find the sum of all elements in a list

l = [10, 20, 30, 40, 50]

#  print(sum(l))

sum=0
for i in l:
    sum+=i

print("sum=",sum)



#3) Find the largest element in a list

l = [10, 50, 20, 80, 30]

print(max(l))

#4) Find the smallest element in a list


l = [10, 50, 20, 80, 30]

print(min(l))

#5) Find the second largest element

l = [10, 50, 20, 80, 30]

l.sort()

print(l[-2])

#6)Find the second smallest element

l = [10, 50, 20, 80, 30]

l.sort()

print(l[1])

#7)Count the number of even and odd numbers

l = [10, 15, 22, 7, 30]

even = 0
odd = 0

for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)

#8)Reverse a list without using reverse()

#9) Check whether a list is sorted

l = [10, 20, 30, 40]

if l == sorted(l):
    print("Sorted")
else:
    print("Not Sorted")

#10)Remove duplicate elements from a list

l = [10, 20, 10, 30, 20, 40]

result = []

for i in l:
    if i not in result:
        result.append(i)

print(result)

#11)Merge two lists

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1 + l2)

#12)Find the common elements in two lists

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

for i in l1:
    if i in l2:
        print(i)

#13)Find elements present in the first list but not the second

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

for i in l1:
    if i not in l2:
        print(i)
#16) Split a list into two equal halves

l = [1, 2, 3, 4, 5, 6]

mid = len(l) // 2

print(l[:mid])
print(l[mid:])

#17)Swap the first and last elements

l = [10, 20, 30, 40, 50]

l[0], l[-1] = l[-1], l[0]

print(l)

#18) Swap two given positions

l = [10, 20, 30, 40, 50]

p1 = 1
p2 = 3

l[p1], l[p2] = l[p2], l[p1]

print(l)

#20) Move all negative numbers to the beginning

l = [3, -2, 5, -7, 1, -4]

result = []

for i in l:
    if i < 0:
        result.append(i)

for i in l:
    if i >= 0:
        result.append(i)

print(result)'''

