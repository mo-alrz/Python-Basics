mass = int(input("Please enter your weight : "))
height = int(input("Please enter your height : "))
BMI = mass / ((height / 100) ** 2)
print("BMI =", BMI)


# Define the function:
def calculate_bmi(mass, height):
    BMI = mass / ((height / 100) ** 2)
    return "BMI = "+str(BMI)


print(calculate_bmi(72, 175))
