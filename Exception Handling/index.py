# If an exception occurs, the code will jump to the except block.
# If no exception occurs, the code will execute the else block.
# The finally block will always execute, regardless of whether an exception occurred or not.

# a = int(input("Enter a number: ")) 
# try:
#     print(10/a)
# except Exception as err:
#     print("Sorry! There was an error as ", err) 
# else:
#     print("No exceptions occurred, the result is:", 10/a)
# finally:
#     print("This block always executes, regardless of exceptions.")

# print("This line will always execute.")

age = int(input("Enter your age: "))

try:
    if age < 10 or age > 18:
        raise ValueError('Your age must be between 10 & 18')
    else:
        print('Welcome to the club')
except Exception as err:
    print(f"An error occurred as {err}")

print('The club will start soon...')