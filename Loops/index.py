# a = range(1,21,1)
# for i in a:
#     print(i)

# The start value and step value is default in range function i.e. set to 1
# for i in range(21):
#     print(i)

# Reversing the loop 
# for i in range(16,1,-1):
#     print(i)


# Printing a table of 5
# n = int(input('Enter the number to print the table: '))
# for i in range(11):
#     print(f'{n} x {i} = {i*n}')

# Loops for strings
# a = 'Sumeet is a billionaire'

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# Some Concepts in Loops

# Continue Statement
# for i in range(21):
#     if i == 15:
#         continue
#     print(i)

# Break and Else statement
for i in range(21):
    if i == 15:
        print('Break Executed') 
        break
    print(i)
else:
    print('Break not Executed')