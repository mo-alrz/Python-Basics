# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

a = int(input("Enter diamond's height: "))
b = int(a / 2 + 1)
if a % 2 != 0:
    for x in range(b):
        print(" " * (b - x), "*" * (2 * x + 1))
    for x in range(b - 2, -1, -1):
        print(" " * (b - x), "*" * (2 * x + 1))
else:
    print("Should be an Odd number")