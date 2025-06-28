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
# for i in range(21):
#     if i == 15:
#         print('Break Executed') 
#         break
#     print(i)
# else:
#     print('Break not Executed')

# Q1
# n = int(input('Please tell a number'))
# for i in range(n):
#     print('Hey')

# Q2
# n = int(input('Please tell a number'))
# for i in range(n+1):
#     print(i)

# Q3
# n = int(input('Please tell a number'))
# for i in range(n+1):
#     print(n-i)

# Q4
# n = int(input('Please tell a number'))
# for i in range(11):
#     print(f'{n} x {i} = {i*n}')

# Q5
# n = int(input('Please tell a number'))
# num = 0
# for i in range(n):
#     num += i 
# print(num)

# Q6
# n = int(input('Please tell a number'))
# num = 1
# for i in range(n):
#     num *= i+1 
# print(num)

# Q7
# n = int(input('Please tell a number'))
# even = 0
# odd = 0
# for i in range(n):
#     if(i%2==0):
#         even+=i
#     else:
#         odd+=i
# print(even, odd)

# Q8
# n = int(input('Please tell a number'))
# for i in range(n):
#     if(n%(i+1)==0):
#         print(i+1)

# Q9
# n = int(input('Please tell a number'))
# sum = 0
# for i in range(n-1):
#     if(n%(i+1)==0):
#         sum+=(i+1)

# if(n == sum):
#     print(f'{n} is a perfect number as sum is {sum}')
# else:
#     print(f'{n} is not a perfect number as sum is {sum}')

# Q10
# n = int(input('Please tell a number'))
# count = 0
# for i in range(n):
#     if(n%(i+1)==0):
#         count+=1

# if(count == 2):
#     print(f'{n} is Prime')
# else:
#     print(f'{n} is not Prime')

# Q11
# str = 'szsjfgzdsjfh'
# revstr = ''
# for i in range((len(str))):
#     revstr += (str[(len(str))-i-1])
# print(revstr)

# Q12
# str = 'oyzgzgro'
# revstr = ''
# for i in range((len(str))):
#     revstr += (str[(len(str))-i-1])

# if(str == revstr):
#     print(f'{str} is a pallindrome')
# else:
#     print(f'{str} is not a pallindrome')
    
# Q13
a = 'sjkjfha38rwij95e;.;drng'
char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1

print(char, dig, spchr)