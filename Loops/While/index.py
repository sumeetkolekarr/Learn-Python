# While Loop 

# a = 1
# while a<=30:
#     print(a)
#     a += 1

# Q1
# a = int(input('Tell Your Number: '))
# while a > 0:
#     print(a%10)
#     a = a // 10

# Q2
# a = int(input('Tell Your Number: '))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# print(rev)

# Q3
# a: int = int(input('Tell Your Number: '))
# copy: int = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# if copy == rev:
#     print('Number is Palindrome')
# else:
#     print('Number is not Palindrome')

# Q4
import random
num = random.randint(1,10)
tries = 0
while True:
    guess = int(input('Please Enter your Number'))
    if num == guess:
        tries+=1
        print(f'You Won in {tries} tries!')
        break
    elif num < guess:
        tries+=1
        print('Go a Little Lower!')
    elif num > guess:
        tries+=1
        print('Go a Little Higher!')
    else:
        tries+=1
        print('You Lose!')