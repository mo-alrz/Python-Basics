# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was

a = int(input("Please enter a number : "))

for i in range(a):
    if i % a == 0 or (i + 1) % a == 0:
        print(a * '%')
    else:
        print('%' + (a - 2) * ' ' + '%')

# OR

for x in range(1):
    print("%" * a)
for x in range(1, a - 1):
    print("%", " " * (a - 4), "%")
for x in range(a - 1, a):
    print("%" * a)
