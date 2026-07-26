# List Comprehension
# l = [i for i in range(1,21) if i %2 == 0]
# print(l)

# a = {i : i**2 for i in range(1,10)}
# print(a)

# Lambda Function 
# add = lambda a :'even' if a % 2 == 0 else "odd"
# print(add(12))

# Map Function 
# a = [1,2,3,4,5]
# doubled = map(lambda x : x*2, a) 
# print(list(doubled))

# Filter Function 
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
    
# a= [1,2,3,4,5]
# result = filter(even, a)
# print(list(result))

# Modules and Packages
from models import maths, hello
hello.hello()
print(maths.add(5,2))