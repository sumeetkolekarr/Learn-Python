#Inbuilt Function
# print('Functions')

# User Defined Function 
# def hello():
#     print('Hello')
# hello()

# Positional Arguments
# def sum(a,b):
#     print(a+b)
# sum(12,12)

# Keyword Arguments
# def hello(name, age):
#     print(name, age)
# hello(age=22, name='Sumeet')

# Default Arguments
# def sum(a,b=12):
#     print(a+b)
# sum(5)

# Example
# def palindrome(st):
#     rev = ''
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
    
#     if rev == st:
#         print('Palindrome')
#     else:
#         print('Not a Palindrome')
# palindrome('onion')

def hello():
    return 'Hello, How are you?'
print(hello())