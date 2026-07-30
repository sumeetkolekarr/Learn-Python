"""
Topic: Lists & Tuples
Goal: comfortable creating, modifying, and querying lists; understand why
tuples are different.
"""

# TODO 1: Create a list of your 5 favorite movies (or books, songs -
# whatever you like). Print the list.
books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Catcher in the Rye"]
print(books)

# TODO 2: Add a new movie to the end of the list with .append(). Insert a
# different movie at position 0 with .insert(). Print the list after each.
books.append("The Hobbit")
print(books)
books.insert(0, "Moby Dick")
print(books)

# TODO 3: Remove one movie from the list by name using .remove(). Print the
# result.
books.remove('The Hobbit')
print(books)

# TODO 4: Sort the list alphabetically and print it. Then reverse it and
# print it again.
books.sort()
print(books)
books.reverse()
print(books)

# TODO 5: Check whether a specific movie is in your list using the `in`
# operator, and print True/False.
if 'The Hobbit' in books: print(True)
else: print(False)

# TODO 6: Create a tuple: coordinates = (10, 20, 30).
# Try to change coordinates[0] = 99 and run the file. Read the error you
# get, then comment it out and write, in a comment, what error it was and
# why tuples behave this way.
coordinates = (10, 20, 30)
# coordinates[0] = 99  # TypeError: 'tuple' object does not support item assignment. Tuples are immutable, meaning their elements cannot be changed after creation.

# TODO 7: numbers = [4, 2, 9, 1, 7, 15, 6]
# Find the SECOND largest number without using sorted()/sort(). Then, as a
# separate line, find it again the easy way using sorted().
numbers = [4, 2, 9, 1, 7, 15, 6]
max_num = max(numbers)
numbers.remove(max_num)
second_largest = max(numbers)
print(second_largest)    
numbers = [4, 2, 9, 1, 7, 15, 6]
print(sorted(numbers)[-2])  # This will print the second largest number using sorted().

# TODO 8: Using a list comprehension, create a list of the even numbers
# from 1 to 20 (no loop, no if/append - one line).
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)