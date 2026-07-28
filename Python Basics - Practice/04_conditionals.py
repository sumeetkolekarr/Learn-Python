"""
Topic: Conditional Statements
Goal: comfortable with if / elif / else and combining conditions.
"""

# TODO 1: age = 25 (change this value and re-test).
# Print "Minor" if under 18, "Adult" if 18-59, "Senior" if 60+.


age=18
if(age<18): 
    print('Minor')
elif(age>17 and age<60):
    print('Adult')
else:
    print('Senior')

# TODO 2: number = 17 (change this value and re-test).
# Print whether it's "Even" or "Odd".
number = 19
print('Odd' if number%2==1 else 'Even')

# TODO 3: a, b, c = 12, 45, 7 (change these and re-test).
# Print the largest of the three, without using max().
a, b, c = 12, 45, 7
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)

# TODO 4: year = 2024 (change this and re-test, e.g. try 1900, 2000, 2023).
# Print whether it's a leap year. Rule: divisible by 4, but not by 100
# unless also divisible by 400.
year = 2023
if(year%4==0 and year%100!=0) or year%400==0:
    print('Leap Year')
else:
    print('Not a Leap Year')

# TODO 5: marks = 82 (change this and re-test).
# Print grade: >=90 "A", >=75 "B", >=50 "C", else "Fail".
marks = 85
if(marks>=90):
    print('A')
elif(marks>74 and marks<90):
    print('B')
elif(marks>49 and marks<75):
    print('C')
else:
    print('Fail')