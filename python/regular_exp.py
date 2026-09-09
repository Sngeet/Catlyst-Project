import re

# re.search()  #find a pattern anywhere in a string

# re.match()    # check fr pattern at the biginning
# re.findall()  # return all matching values
# re.sub()      # replace matching text

# email= "sangeeth@gmail.com"
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.match(pattern,)



# 1. \d -> digit  matches any digit from 1-9
# re.findall(r"\d", "age 25")  #['2', '5']

# re.findall(r"\d+", "i have 25 apple and 10 orange")  #['25', '10']

# #2) \w -> word character means words , number, unde square

# print(re.findall(r"\w", "hi_25") ) #['h', 'i', '_', '2', '5']

#3) \s white space means space tab next line
# re.findall(r"\s", "age is")  # [" "]

#4) . -> any character means matches almost any single character
#  re.findall(r".", "abc")  #['a','b','c']

# print(re.findall(r"c.t", "cat cot cut") )  #['cat', 'cot', 'cut']
    # means any one character b/w c and t

# 6) * means zero or more occurrence
# print(re.findall(r"ab*", "a ab abb abbbb abbbb")) #['a', 'ab', 'abb', 'abbbb', 'abbbb']

# b* means zero or more b's

#7) ? -> zero or one  means the character is optional
print(re.findall(r"colou?r", "color colour"))