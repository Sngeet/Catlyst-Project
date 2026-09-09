#)
# syntx= {key_expression: value expression for item in iterable}

# l= [1,2,3,4,5]
# new={i:i*3 for i in l}
# print(new)

#o/p
#{1: 3, 2: 6, 3: 9, 4: 12, 5: 15}

#square

# num=[1,2,3,4,5]
# sq={i:i**2 for i in num }
# print(sq)

#o/p
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#cube

# num=[1,2,3,4,5]
# cb={i:i**3 for i in num }
# print(cb)

#o/p
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

#using condition

#even 

# ev={x:"even" for x in range (10) if x%2==0  }
# print(ev)

#o/p
# {0: 'even', 2: 'even', 4: 'even', 6: 'even', 8: 'even'}

#odd
# ev={x:"odd" for x in range (10) if x%2==1  }
# print(ev)

# o/p
# {1: 'odd', 3: 'odd', 5: 'odd', 7: 'odd', 9: 'odd'}

# ev={x:x for x in range (10) if x%2==0  }
# print(ev)
#o/p
# {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

# odd or even
# res={x: "even" if x%2==0 else "odd"  for x in range(1,4)}
# print(res)

#o/p  {1: 'odd', 2: 'even', 3: 'odd'}

#swap
# student={
#     "name": "john",
#     "age" :22,
#     "course":"python"
# }
# swapped= {value: key for key, value in student.items()}
# print(swapped)

#o/p
#{'john': 'name', 22: 'age', 'python': 'course'}

'''practice'''

#1)
# num=[1,2,3,4,5]
# sq={i:i**2 for i in num }
# print(sq)

