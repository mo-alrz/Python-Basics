speed_in_Mph = int(input('Enter ur speed in Mph : '))
print("your Speed in KMph =", speed_in_Mph * 1.60934)


# Define function
def mile_to_km(speed_in_mph):
    return "your Speed in KMph = " + str(speed_in_mph * 1.60934)


print(mile_to_km(1))
