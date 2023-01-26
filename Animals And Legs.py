chickens = int(input('Enter the number of chickens: '))
pigs = int(input('Enter the number of pigs: '))
sum_of_legs = chickens * 2 + pigs * 4
print("Total legs that pigs and chickens together have:" , int(sum_of_legs))


def legs(chicken,pig):
    return f'Total legs that pigs and chickens together have: ' \
           f'{chickens * 2 + pig * 4}'


print(legs(2,4))
