ch = 14 * 60 * 60
cm = 34 * 60
cs = 42
ld = ch + cm + cs
td = 24 * 60 * 60
print('Seconds left of the day :', td - ld)


# Define Function:
def seconds_of_a_day_remained(h, m, s):
    secs_in_a_day = 24 * 60 * 60
    hours = h * 60 * 60
    mins = m * 60
    secs = s
    secs_left = secs_in_a_day - (hours + mins + secs)
    return f'Seconds left of the day : {secs_left}'


print(seconds_of_a_day_remained(14, 34, 42))
