"""
Topic: Loops (for / while)
Goal: comfortable iterating, accumulating results, and controlling loops
with break/continue.
"""

# TODO 1: Print numbers 1 to 20 using a for loop.
for i in range(1,21): print(i)

# TODO 2: Print only the even numbers from 1 to 50.
for i in range(1,51): 
    if i%2==0: print(i)

# TODO 3: Calculate and print the sum of numbers from 1 to 100 using a loop
# (don't use the sum() shortcut - build the total yourself).
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

# TODO 4: Print the multiplication table of 7, from 7x1 to 7x10, one line
# each, e.g. "7 x 1 = 7".
num = 7
for i in range(1,11): print(f'{num} x {i} = {num*i}')

# TODO 5: Use a while loop to count down from 10 to 1 (printing each
# number), then print "Liftoff!" after the loop ends.
i=10
while(i>0):
    print(i)
    i-=1
else:
    print('Liftoff!')

# TODO 6: numbers = [23, 6, 45, 12, 89, 34]
# Find the maximum value using a loop, WITHOUT using max().
numbers = [23, 6, 45, 12, 89, 34]
max = numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
print(max)

# TODO 7: Print this pattern using a loop (5 rows):
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print(i*'*')


# TODO 8: numbers = [3, 8, 1, 7, 4, 9, 2]
# Loop through and stop (break) as soon as you find the number 7. Print a
# message when you find it.
number = [3, 8, 1, 7, 4, 9, 2]
for i in number:
    if i == 7: 
        print('7 found')
        break


# TODO 9: Print all numbers from 1 to 20 EXCEPT multiples of 3, using
# continue to skip them.
for i in range(1,21):
    if(i%3!=0):
        print(i)
    else: 
        continue
