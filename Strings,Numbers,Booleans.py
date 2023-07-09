# print built-in function

# 1 - Strings :
print("Hello, World!")  # Prints the string "Hello, World!" to the terminal window.

# 1 - 1 Concatenation
print("Py" + "Charm")  # Prints PyCharm

# 1 - 2 Concat string with number
print("My favorite number is: " + str(7))  # Prints My favorite number is: 7

# 1 - 3 String methods
my_string = 'HeLlO wOrLd'
print(my_string.capitalize())  # Capitalize the first letter and convert the remaining letters to lowercase
print(my_string.upper())  # Capitalize all letters
print(my_string.lower())  # Lowercase all the letters
print(my_string.casefold())  # Like lower but stronger, for all languages and symbols
print(my_string.swapcase())  # Change the uppercase to lowercase and vice versa
print(my_string.title())  # Capitalize the first letter of every world
print(my_string.strip()) # Delete the unwanted saces or any other characters


# 2 - Numbers :
# 2 - 1 Integers
print(42)  # Prints 42 to the terminal window.
print(-42)  # Prints -42 to the terminal window.
print(0)  # Prints 0 to the terminal window.

# 2 - 2 Floats :
# Leading and closing zero is not mandatory
print(3.141592)  # Prints 3.141592 to the terminal window.
print(.5)  # Prints 0.5 to the terminal window.
print(5.)  # Prints 5.0 to the terminal window.

# Arithmetic operations
print(1 + 1)  # Prints 2
print(5 - 2)  # Prints 3
print(3 * 4)  # Prints 12
print(6 / 2)  # Prints 3.0
print(5 / 2)  # Prints 2.5
print(5 // 2)  # Prints 2
print(5 % 2)  # Prints 1

# 3 - Boolean Operators :
print(True)  # Prints True
print(False)  # Prints False

# 3 - 1 Negation
print(not True)  # Prints False
print(not False)  # Prints True

# 3 - 2 And
print(True and True)  # Prints True
print(True and False)  # Prints False
print(False and True)  # Prints False
print(False and False)  # Prints False

# 3 - 3 Or
print(True or True)  # Prints True
print(True or False)  # Prints True
print(False or True)  # Prints True
print(False or False)  # Prints False
