#1) Print the length of the string
text = "Python Full Stack"
print(len(text))

#2)Convert to uppercase

text = "hello world"
print(text.upper())

#3)Convert to lowercase

text = "PYTHON"
print(text.lower())

#4)Capitalize the first letter

text = "python programming"
print(text.capitalize())

#5)Count how many a

text = "banana"
print(text.count("a"))

#6)Check Python starts with Py

text = "Python"
print(text.startswith('Py'))

#7)Replace Java with Python

text = "I love Java"
print(text.replace("Java", "Python"))

#8)Remove spaces from both end

text = " Hello World "
print(text.strip())

#9)Check a string contains only digits

text = input("Enter a string: ")
print(text.isdigit())

#10)Check a string contains only alphabets

text = input("Enter a string: ")

print(text.isalpha())

#11)Check a password is strong

password = input("Enter password: ")

if len(password) > 8:
    print("Strong Password")
else:
    print("Weak Password")