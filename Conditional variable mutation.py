def conditional_var_mut(a,is_bonus = False):
    output1 = 0
    output2 = ''
    c = 123

    if a % 2 == 0:
        output1 +=1
        return output1

    if a % 2 != 0 and 10 < a < 20 :
        output2 = output2 + 'Sweet'

    elif a % 2 != 0 and a < 10 :
        output2 = output2 + 'Less'

    elif a % 2 != 0 and a > 20:
        output2 = output2 + 'More'
    return output2

print(conditional_var_mut(4))
print(conditional_var_mut(5))
print(conditional_var_mut(11))
print(conditional_var_mut(21))
