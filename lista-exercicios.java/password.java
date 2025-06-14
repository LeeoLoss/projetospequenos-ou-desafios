import java.util.Scanner;
public class password {
    public static void main(String[] args) {

        System.out.println("Password: ");

        Scanner sc = new Scanner(System.in);
        int password = sc.nextInt();

        while (password != 2002) {
            System.out.println("Password incorrect.");
            password = sc.nextInt();
        }
        System.out.println("Welcome.");

        sc.close();
    }
}
