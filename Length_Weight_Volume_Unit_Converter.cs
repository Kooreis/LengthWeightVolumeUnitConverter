```CSharp
using System;

namespace UnitConverter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Unit Converter");
            Console.WriteLine("1. Length");
            Console.WriteLine("2. Weight");
            Console.WriteLine("3. Volume");
            Console.Write("Choose an option: ");
            int option = Convert.ToInt32(Console.ReadLine());

            switch (option)
            {
                case 1:
                    Console.Write("Enter length in meters: ");
                    double length = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine("Length in feet: " + length * 3.28084);
                    break;
                case 2:
                    Console.Write("Enter weight in kilograms: ");
                    double weight = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine("Weight in pounds: " + weight * 2.20462);
                    break;
                case 3:
                    Console.Write("Enter volume in liters: ");
                    double volume = Convert.ToDouble(Console.ReadLine());
                    Console.WriteLine("Volume in gallons: " + volume * 0.264172);
                    break;
                default:
                    Console.WriteLine("Invalid option");
                    break;
            }
        }
    }
}
```