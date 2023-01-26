l = float(input("Enter length :"))
w = float(input("Enter width :"))
h = float(input("Enter height :"))
print("Volume =", l * w * h)
print("Surface Area =", 2 * l * w + 2 * w * h + 2 * l * h)


# Define the function:
def vol_and_surface_area(l, w, h):
    vol = float(l * w * h)
    surface_area = 2 * float(l * w + w * h + l * h)
    return f'Volume = {vol} \nsurface area = {surface_area}'


print(vol_and_surface_area(1, 2, 3))
