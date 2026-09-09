#break
for i in range(10):
    if i==4:
        break
    print(i)
print()
#continue
for i in range(10):
    if i==4:
        continue
    print(i)
print()
    #pass

for i in range(10):
    if i==4:
        pass
    print(i)
print()

#while true
while True:
    name=input("enter your name:(or enter 'exit' to exit from loop)")
    if name=='exit':
        break
    print("hello",name)
print()

