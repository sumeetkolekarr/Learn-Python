"""
Topic: Data Types & Type Conversion
Goal: recognize Python's basic types and convert between them deliberately.
"""

# TODO 1: Create one variable each of type int, float, str, bool. Print the
# type() of each one.
from xxlimited import Str


num = 5
float = 2.9
str = 'a'
bool = True
print(type(num), type(float), type(str), type(bool))

# TODO 2: Use input() to ask the user for their age (this comes in as a
# string). Convert it to int and print "In 5 years you'll be <age+5>".
age = input('Enter Your Age: ')
age = int(age)
print(f'In 5 years you will be {age + 5} with billions in your bank account')

# TODO 3: Convert the float 9.99 to an int and print it. In a comment below,
# write one line explaining what happened to the decimal part.
fl = 9.99
fl = int(fl)
print(fl)
# The conversion returns answer in floor and that is why the decimal part is omitted

# TODO 4: Convert the string "123" to an int, add 27 to it, and print the
# result.
strn = '123'
strn = int(strn) + 27
print(strn)

# TODO 5: Convert True and False to int using int(). Print both. In a
# comment, note what numbers they become.
print(int(True), int(False))
# The reason it prints 1 for True and 0 for False is because it follows Digital Logic Paradigm where 1 means something is on i.e. true and 0 means something is off i.e. false

# TODO 6: Convert the number 42 to a string and concatenate it with
# "The answer is: " (use str(), not an f-string, for this one).
num = 42
print('The answer is:', Str(num))