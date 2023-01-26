a = int(input("Please enter girls number: "))
b = int(input("Please enter boys number: "))

if a == b and a + b >= 20:
    print("The party is excellent")
elif a + b >= 20 and a / b != 1:
    print("Quiet a cool party")
elif a + b < 20:
    print("Average party")
elif a == 0:
    print("Sausage party")
