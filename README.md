# Python Documentation

# Python Conversion Script

This Python script provides a simple interface for converting between different units of length, weight, and volume. The script does not require any external libraries, making it easy to run on any system with Python installed.

## Features

The script provides three main functionalities:

1. **Length Conversion**: This feature allows the user to convert between millimeters, centimeters, meters, and kilometers. The user is prompted to enter a value and the unit they wish to convert from, and the script will output the converted value in the desired unit.

2. **Weight Conversion**: This feature allows the user to convert between grams, kilograms, pounds, and ounces. Similar to the length conversion, the user is prompted to enter a value and the unit they wish to convert from, and the script will output the converted value in the desired unit.

3. **Volume Conversion**: This feature allows the user to convert between milliliters, liters, cubic meters, and cubic feet. The user is prompted to enter a value and the unit they wish to convert from, and the script will output the converted value in the desired unit.

## Usage

To use the script, simply run it in your Python environment. You will be presented with a menu of options for what type of conversion you want to perform (length, weight, or volume). After selecting an option, you will be prompted to enter the value you wish to convert and the unit you are converting from. The script will then output the converted value in the new unit.

## Libraries

This script does not use any external libraries. It only uses the built-in Python libraries for basic operations such as input/output and arithmetic operations.

---

# C# Documentation

# Unit Converter in C#

This repository contains a simple console application written in C# that converts units of length, weight, and volume from metric to imperial system.

## Program Description

The program presents the user with three options: 

1. Convert length from meters to feet
2. Convert weight from kilograms to pounds
3. Convert volume from liters to gallons

The user is prompted to choose an option and then enter the value they wish to convert. The program then performs the conversion and displays the result.

## Code Explanation

The script is written in C# and uses the `System` namespace, which provides fundamental classes to base your application upon.

Here is a brief explanation of the key components of the script:

- `Console.WriteLine()`: This method is used to output strings to the console. It is used to display the welcome message and the conversion options to the user.

- `Console.ReadLine()`: This method is used to read the user's input. It is used to get the user's chosen option and the value they wish to convert.

- `Convert.ToInt32()` and `Convert.ToDouble()`: These methods are used to convert the user's input, which is read as a string, to the appropriate numeric type for calculations.

- `switch` statement: This is used to perform different actions based on the user's chosen option.

## Usage

To run the program, you need a C# compiler. If you have the .NET SDK installed, you can use the `dotnet run` command in the terminal from the directory where the script is located.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

# Java Documentation

# Unit Converter in Java

This Java script is a simple console-based Unit Converter. It allows the user to convert units of Length, Weight, and Volume. The user is presented with a menu to choose the type of conversion they want to perform. After selecting the type, they are prompted to enter the value to be converted. The script then performs the conversion and displays the result.

## Script Explanation

The script begins by importing the `java.util.Scanner` class, which is a part of the Java's utility package. This class is used to read the input provided by the user when running the program.

The main function of the script is enclosed within the `UnitConverter` class. Inside the `main` method, an instance of the `Scanner` class is created to read the user's input.

The user is then presented with a menu to choose the type of conversion they want to perform. The `switch` statement is used to perform different actions based on the user's choice.

- If the user chooses `1`, they are asked to enter a value in meters. The script then converts this value into feet and inches.
- If the user chooses `2`, they are asked to enter a value in kilograms. The script then converts this value into pounds and ounces.
- If the user chooses `3`, they are asked to enter a value in liters. The script then converts this value into gallons and cubic feet.

If the user enters a choice that is not in the menu, the script displays "Invalid choice".

After performing the conversion, the script closes the `Scanner` object.

## Libraries Used

- `java.util.Scanner`: This class is a part of Java's utility package. It is used to read the input provided by the user when running the program. It provides methods to parse primitive types and strings using regular expressions, which can be used to break the input into tokens.

---
