def sum_and_average(n):
    my_sum = 0
    for i in range(n):
        a = int(input("Enter a number : "))
        my_sum = my_sum + a
    print('Sum :', my_sum, '\n' + 'Average :', my_sum / n)


sum_and_average(3)
