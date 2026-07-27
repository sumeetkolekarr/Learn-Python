"""
Topic: Variables & Operators
Goal: get comfortable creating/naming variables and using arithmetic,
comparison, and logical operators.
"""

# TODO 1: Create variables for your name, age, and city. Print one sentence
# that uses all three, using an f-string.
name = "Sumeet"
age = 23
city = "Kolhapur"
print(f"My name is {name}, I am {age} years old and I live in {city}")


# TODO 2: Swap the values of two variables a = 5 and b = 10, WITHOUT using a
# third variable. Print both after swapping to prove it worked.
a = 5
b = 10
a, b = b ,a 
print(f"a = {a}, b = {b}")

# TODO 3: price = 250, quantity = 4. Calculate and print the total cost.
price = 250
quantity = 4
cost = price * quantity
print(cost)

# TODO 4: Print the quotient and the remainder when 47 is divided by 6
# (two separate print statements, using // and %).
quotient = 47//6
remainder = 47%6
print(quotient)
print(remainder)

# TODO 5: num = 17. Using comparison + logical operators, print True/False
# for: "num is greater than 10 AND less than 20".
num = 17
print(num>10 and num<20)

# TODO 6: Pick any two numbers. Print the result of both / and // on them
# in the same run, so the difference between the two is visible.
c = 5
d = 2
print(5/2, 5//2)