"""
Capstone: Contact Book (CLI)
Goal: combine dictionaries, functions, loops, conditionals, and exception
handling into one small program. This ties together everything from
files 01-09.

Requirements:
- Store contacts as a dictionary: {"name": "phone number", ...}
- Show a menu in a loop:
    1. Add contact
    2. Search contact
    3. Delete contact
    4. List all contacts
    5. Exit
- Keep looping until the user picks Exit.
- Handle bad input gracefully (e.g. searching for a name that doesn't
  exist, or typing a menu option that isn't 1-5) instead of crashing.

Stretch goal (optional, do this last): save contacts to a file
(contacts.txt) so they're still there next time you run the program -
you'll need file handling from 10_file_handling.py for this.
"""

contacts = {}


def add_contact():
    # TODO: ask for a name and a phone number, store them in `contacts`
    pass


def search_contact():
    # TODO: ask for a name, print the phone number if found, else say
    # "not found" (don't let a missing key crash the program)
    pass


def delete_contact():
    # TODO: ask for a name, remove it from `contacts` if present, else say
    # "not found"
    pass


def list_contacts():
    # TODO: print every contact as "name: phone", or "No contacts yet" if
    # the dictionary is empty
    pass


def main():
    while True:
        print("\n1. Add  2. Search  3. Delete  4. List  5. Exit")
        # TODO: get the user's choice, and call the right function above
        # based on it. Break out of the loop when they choose Exit.
        pass


if __name__ == "__main__":
    main()
