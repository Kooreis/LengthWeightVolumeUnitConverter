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