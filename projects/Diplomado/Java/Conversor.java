import java.util.Scanner;
import java.math.BigDecimal; 
import java.math.RoundingMode; 

public class Conversor {
    public static void main(String[] args) {
        Scanner conver = new Scanner(System.in);
        double tasa;
        double money;

        System.out.println("¡Bienvenido! con este pequeño programa podrás convertir tus bolívares a dólares americanos.");
        
        // El programa funciona, pero el usuario DEBE usar el punto.
        System.out.println("Por favor introduce tu monto en bolívares. (Usar punto \".\"):");
        money = conver.nextDouble(); 

        System.out.println("¿Cuál es la tasa vigente? (Usar punto \".\"):");
        tasa = conver.nextDouble();

        double resultado = money / tasa;

        BigDecimal resBigDecimal = new BigDecimal(String.valueOf(resultado));
        
        resBigDecimal = resBigDecimal.setScale(2, RoundingMode.HALF_UP);

        System.out.println("La cantidad ingresada en dólares equivale a " + resBigDecimal + " dólares americanos.");

        conver.close();
    }
}