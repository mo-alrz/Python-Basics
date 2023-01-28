# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was


h = int(input("Enter pyramid's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
