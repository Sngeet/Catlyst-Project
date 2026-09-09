#syntax 

#new_list=[expressin for]

#eg

# number=[1,2,3,4,5]
# new=[i*2 for i in number]
# print(new)

#Square

# number=[1,2,3,4,5]
# new=[i*i for i in number]
# print(new)

#using range

# n=[x for x in range(1,6)]
# print(n)

# convert string to upper case

# s= "hello"
# result = [i.upper() for i in s]
# print(result)

#even
# number=[1,2,3,4,5]
# even=[num for num in number if num%2==0]
# odd=[num for num in number if num%2==1]
# print("odd =", odd, "even = ",even)

#odd or even
# number=[1,2,3,4,5]
# res=["even" if num%2==0 else "odd" for num in number]
# print(res)

#o/p
# ['odd', 'even', 'odd', 'even', 'odd']

#number greater than 10
# number=[1,20,30,48,5]
# res=[num for num in number if num > 10]
# print(res)

#+ve -ve

# number=[1,-2,3,4,-5]
# res=["+ve" if num>0 else "-ve" for num in number]
# print(res)

#o/p
#['+ve', '-ve', '+ve', '+ve', '-ve']



# work

#1,2)
# number=[]
# for i in range(0,21):
#     number.append(i)
# even=[num for num in number if num%2==0]
# print(even)
# odd=[num for num in number if num%2==1]
# print(odd)

#3)
# nums = [1, 2, 3, 4, 5]
# new=[i*5 for i in nums]
# print(new)

#4)
# names = ["apple", "banana", "mango"]
# leng = [len(word) for word in names]
# print(leng)

#5)
# names = ["apple", "banana", "mango"]
# leng = [word.upper() for word in names]
# print(leng)

#6)
# numbers = [num for num in range(1, 51) if num % 5 == 0]
# print(numbers)

#7)
# nums = [10, 15, 20, 25, 30]
# new = [i for i in nums if i > 20]
# print(new)

# number=[-1,2,3,-4,5]
# n=[num for num in number if num>0]
# p=[num for num in number if num<1]
# print("-ve =", p, "+ve = ",n)