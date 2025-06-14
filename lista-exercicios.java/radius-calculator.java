public class MediaPonderada {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner raio = new Scanner(System.in);

        double R, A;
        double pi = 3.14159;

        R = raio.nextDouble();

        A = pi * R * R;

        System.out.printf("A=%.4f%n", A);

        raio.close();
    }
}
