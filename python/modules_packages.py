#1)#import complete module

import mathop
print(mathop.add(5,4))

#2) import specific function
# from mathop import div 
# print(div(20,4))

#3)import multiple function

# from mathop import div,add
# print(div(20,4))
# print(add(20,4))

#4) import everything
from mathop import *
print(div(20,4))
print(add(20,4))
print(sub(20,4))
print(mul(20,4))
print(PI)

#5)import with alias 

# means we can give short names to the function