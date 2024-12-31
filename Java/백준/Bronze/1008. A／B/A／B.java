import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] values = input.nextLine().split(" ");

        Double a = Double.parseDouble(values[0]);
        Double b = Double.parseDouble(values[1]);

        System.out.println(a / b);
    }
}