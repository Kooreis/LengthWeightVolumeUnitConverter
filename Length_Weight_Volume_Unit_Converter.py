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