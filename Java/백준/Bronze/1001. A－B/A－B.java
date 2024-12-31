import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] values = input.nextLine().split(" ");

        int a = Integer.parseInt(values[0]);
        int b = Integer.parseInt(values[1]);

        System.out.println(a - b);
    }
}