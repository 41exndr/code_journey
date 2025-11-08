import java.util.*;

public class Balance {
    public static void main(String[] args) {
        Scanner robot = new Scanner(System.in);
        double dinero;

        System.out.println("Por favor ingresa el balance inicial...");
        dinero = robot.nextInt();
        System.out.println("¡Hecho! tienes " + dinero + " en tu cuenta. Ahora, ¿qué deseas hacer? Elige una opción!");
        System.out.println("1. Consultar saldo. \n" +
                           "2. Ingresar dinero. \n" +
                           "3. Sacar dinero. \n" +
                           "4. Salir del programa.");

        int opcionSelec = robot.nextInt();

        switch (opcionSelec){
            case 1:
                System.out.println("Tienes " + dinero + " de saldo.");
                break;
            case 2:
                System.out.println("¿Cuánto deseas ingresar?");
                double MasDinero = robot.nextDouble();
                dinero += MasDinero;
                System.out.println("Tienes " + dinero + " de saldo.");
                break;
            case 3:
                System.out.println("¿Cuánto deseas retirar?");
                double MenosDinero = robot.nextDouble();
                dinero -= MenosDinero;
                System.out.println("Tienes " + dinero + " de saldo.");
                break;
            case 4:
                System.out.println("Saliendo del programa");
                break;
            default:
                System.out.println("Opción inválida.");
        }
            robot.close();
        }

    }
