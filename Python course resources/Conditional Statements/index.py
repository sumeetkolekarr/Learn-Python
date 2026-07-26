# a = int(input('Please Provide me number'))

# if a>10:
#     print('Enter A')
    
# elif a == 12:
#     print('You Won')
    
# else:
#     print('Enter B')
    
# Q1
# num1 = 32
# num2 = 23

# if num1 > num2:
#     print(num1)
# elif num1<num2:
#     print(num2)
# else:
#     print('Numbers are Equal')

# Q2
# gen = input('Enter your Gender: ')
# if gen == 'M' or gen =='m':
#     print('Hello Sir')
# elif gen =='F' or gen == 'f':
#     print('Hello Mam')
# else:
#     print('Unidentified Gender')

# Q3
# num = 5
# if num%2==0:
#     print('Even')
# else:
#     print('Odd')

# Q4
# name = input('Enter your Name: ')
# num = int(input('Enter your Age: '))

# if num>18:
#     str = 'You are a valid Voter'
# else: 
#     str = 'You are not a valid Voter'
    
# print(f"Hello {name}, {str}")

# Q5
# year = int(input('Enter you Year: '))

# if year%100 == 0 and year%400 == 0:
#     print('Its a leap year')
# elif year%100 != 0 and year%4 == 0:
#     print('Its a leap year')
# else:
#     print('Its a Normal Year')

# Q6
temp = 25

if(temp>40):
    print('Very Hot')
elif temp>30 and temp<40:
    print('Hot')
elif temp>20 and temp<30:
    print('Pleasant')
elif temp>10 and temp<20:
    print('Cold')
elif temp>0 and temp<10:
    print('Cold')
else:
    print('Freezing Cold')