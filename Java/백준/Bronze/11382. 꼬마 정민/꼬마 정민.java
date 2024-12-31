import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] values = input.nextLine().split(" ");

        Long a = Long.parseLong(values[0]);
        Long b = Long.parseLong(values[1]);
        Long c = Long.parseLong(values[2]);

        System.out.println(a + b + c);
    }
}