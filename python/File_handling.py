'''modes'''
#1) read = r
#2) write = w
#3) append = a
#4) create = x

# f=open('sample.txt','w')
# f.write("hello")
# f=open('sample.txt','a')
# f.write("\ngood morning")
# f=open('sample.txt','w')
# f.write("\nhello")
# f.close()



# file=open("filename.txt","mode")
# modes are:
# "r"=read(defult)
# "w"=write
# "a"=append
# "x"=create


# f=open("handling.txt","w")
# f.write("hello")
# f=open("handling.txt","a")
# f.write("\ngood morning")
# f=open("handling.txt","r")
# print(f.seek(2))
# content=f.read()
# content1=f.readline()
# print(content)
# print(content1)
# f.close()

# f=open('handling.txt','w')
# f.write("hello everyone")
# f=open('handling.txt','a')
# f.write("\ngood morning")
# f.close()
# with open("handling.txt","r") as file:
#     file.seek(4)
#     print(file.readline())
#     file.seek(7)
#     print(file.readlines())


#qeustions
# # 1.Create a file named student.txt and write your name, age, and course into it.

# f=open('student.txt','w')
# f.write("sangeeth\n21\nPythonfullstack\n")
# f.close()
 
# # 2.Open student.txt and display its complete contents.

# f=open('student.txt','r')
# content=f.read()
# print(content)
# f.close()
 
# # 3.Write 5 student names into a file, one name per line. Then read and display them.

# f=open('student.txt','a')
# f.write("\naseem\nsidarth\nmuhammad\nshamil\nshefin\n")
# f=open('student.txt','r')
# content=f.read()
# print(content)
# f.close()

# f=open('student.txt','r')
# l=0
# for i in f:
#     l+=1
# f.close()
# print(l)
 
# # 4.Create a file numbers.txt containing numbers from 1 to 10. Read the file and calculate their sum.

# f=open('filenumbers.txt','w')
# for i in range(1,11):
#     f.write(str(i)+'\n')
# f.close()

# f=open('filenumbers.txt','r')
# content=f.read()
# print(content)
# f.close()

# f=open('filenumbers.txt','r')
# t=0
# for i in f:
#     t+=int(i)
# f.close()

# print(t)
 
# # # 5.Open a file and count the number of lines in i

# f=open('filenumbers.txt','r')
# c=0
# for i in f:
#     c+=1
# f.close()
# print()
# print(c)