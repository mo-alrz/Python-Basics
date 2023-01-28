# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was


a = int(input("Please enter a number : "))

for i in range(a):
    if i % a == 0 or (i + 1) % a == 0:
        print(a * '%')
    else:
        print('%'+(i-1)*' '+'%'+(a-i-2)*' '+'%')
