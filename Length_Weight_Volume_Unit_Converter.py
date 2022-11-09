```python
def length_conversion():
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Meters")
    print("3. Meters to Kilometers")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        mm = float(input("Enter length in millimeters: "))
        cm = mm / 10
        print("Length in centimeters: ", cm)
    elif choice == 2:
        cm = float(input("Enter length in centimeters: "))
        m = cm / 100
        print("Length in meters: ", m)
    elif choice == 3:
        m = float(input("Enter length in meters: "))
        km = m / 1000
        print("Length in kilometers: ", km)

def weight_conversion():
    print("1. Grams to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Pounds to Ounces")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        g = float(input("Enter weight in grams: "))
        kg = g / 1000
        print("Weight in kilograms: ", kg)
    elif choice == 2:
        kg = float(input("Enter weight in kilograms: "))
        lb = kg * 2.20462
        print("Weight in pounds: ", lb)
    elif choice == 3:
        lb = float(input("Enter weight in pounds: "))
        oz = lb * 16
        print("Weight in ounces: ", oz)

def volume_conversion():
    print("1. Milliliters to Liters")
    print("2. Liters to Cubic Meters")
    print("3. Cubic Meters to Cubic Feet")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ml = float(input("Enter volume in milliliters: "))
        l = ml / 1000
        print("Volume in liters: ", l)
    elif choice == 2:
        l = float(input("Enter volume in liters: "))
        m3 = l / 1000
        print("Volume in cubic meters: ", m3)
    elif choice == 3:
        m3 = float(input("Enter volume in cubic meters: "))
        ft3 = m3 * 35.3147
        print("Volume in cubic feet: ", ft3)

while True:
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Volume Conversion")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        length_conversion()
    elif choice == 2:
        weight_conversion()
    elif choice == 3:
        volume_conversion()
    elif choice == 4:
        break
```