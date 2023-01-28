# Write a program that asks for a number
# It would ask this many times to enter an integer
# If all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

final_sum = 0
n = int(input("How many numbers you would like to enter : "))
for i in range(n):
    s = int(input(f"Number {str(i+1)} : "))
    final_sum += s
average = final_sum / n
print(f'The sum of numbers is {final_sum} and the average is {average}')
