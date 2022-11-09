```java
import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose type of conversion \n 1. Length \n 2. Weight \n 3. Volume");
        int choice = scanner.nextInt();
        switch (choice) {
            case 1:
                System.out.println("Enter value in meters");
                double meters = scanner.nextDouble();
                System.out.println("In feet : " + meters * 3.28084);
                System.out.println("In inches : " + meters * 39.3701);
                break;
            case 2:
                System.out.println("Enter value in kilograms");
                double kilograms = scanner.nextDouble();
                System.out.println("In pounds : " + kilograms * 2.20462);
                System.out.println("In ounces : " + kilograms * 35.274);
                break;
            case 3:
                System.out.println("Enter value in liters");
                double liters = scanner.nextDouble();
                System.out.println("In gallons : " + liters * 0.264172);
                System.out.println("In cubic feet : " + liters * 0.0353147);
                break;
            default:
                System.out.println("Invalid choice");
        }
        scanner.close();
    }
}
```