a = int(input("Enter a number : "))
b = int(a / 2)
for x in range(1, a + 1):
    if x % 2 != 0:
        print("% " * (b + 1))
    else:
        print(" %" * (b + 1))
