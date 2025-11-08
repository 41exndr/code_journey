import java.util.*;

public class IntroData {
    public static void main(String[] args) {
        Scanner lectu = new Scanner(System.in);
        System.out.println("¿Cuál es tu nombre?");
        String nombre = lectu.nextLine();
        System.out.println("¿Cuál es tu edad?");
        int edad = lectu.nextInt();
        System.out.println("Hola " + nombre + ", tienes " + edad + " años!");

        
        // **Buena práctica:** Cerrar el objeto Scanner
        lectu.close();
    }
}
