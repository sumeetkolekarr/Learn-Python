"""
Topic: Strings
Goal: comfortable with string methods, slicing, and basic manipulation.
"""

# TODO 1: Store your full name in a variable. Print it in uppercase, then
# in lowercase.
name = "John Doe"
print(name.upper())
print(name.lower())

# TODO 2: Print the length of your name.
print(len(name))

# TODO 3: Print just the first 3 letters of your name using slicing.
print(name[0:3])

# TODO 4: Print your name reversed, using slicing (no loops, no reversed()).
print(name[::-1])

# TODO 5: sentence = "python is fun"
# Replace "fun" with "powerful" and print the new sentence.
sentence = "python is fun"
sentence = sentence.replace('fun', 'powerful')
print(sentence)

# TODO 6: Check whether the word "python" appears in `sentence` using the
# `in` operator, and print True/False.
print('python' in sentence)

# TODO 7: Split `sentence` into a list of individual words. Print the list.
words = sentence.split()
print(words)

# TODO 8: Join those words back into one string, separated by "-" instead
# of spaces (e.g. "python-is-fun"). Print it.
statement = '-'.join(words)
print(statement)
