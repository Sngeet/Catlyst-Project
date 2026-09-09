a="hai every"
print(a[1])
print(a[-1])
print(a[:3])
print(a[0:-7])
print(a[::2])
print(a[::-1])
print(a[:-7:-1])
print(a[2:])
print(len(a))
print(a.capitalize())
print(a.upper())
print(a.islower())
a='HAI EVERY'
print(a.lower())

print(a.islower())
print("a".isalpha())
print(a.isdigit())
b="hai every"
print(b.index('e'))
print(b.index('e',3)) #start with index 3
#print(b.center('20'))''' #to give space between ch

b="hai every"
print(b.count('e'))
print(b.center(20))

'''c="  haiiiiii"
print(c.strip()) # remove first white space
a="haii"
print(a.startswith('h')) #check is this sentece start with h
a="hello everyone"
print(a.replace("everyone","world"))'''  #to replace a word 

#formating

'''print('{:<10}{:<10}'.format('hello',"world")) #left align
print('{:>10}{:>10}'.format('hello','world')) #right align
print('{:^10}{:^10}'.format('hello','world')) #center align
print('{:>10}{:<10}'.format('hello','world')) #left rigt align'''