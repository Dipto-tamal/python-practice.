import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello Java!");
        System.out.println("This code runs directly in VS Code.");

        Scanner input = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = input.nextLine();

        System.out.print("Enter your age: ");
        int age = input.nextInt();

        System.out.println("\n---- Output ----");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);

        System.out.println("Java is working perfectly! 🚀");

        input.close();
    }
}
