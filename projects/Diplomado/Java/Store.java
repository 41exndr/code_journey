//Ejemplos de constructor y su uso en main

public class Store {
  // instance fields
  String productType;
    
  // constructor method
  public Store(String product) {
    productType = product;
  }
    
  // Add advertise method below
public void advertise() {
    System.out.println("Come spend some money!");
    System.out.println("Selling " + productType + "!");
}

public class Main {
  public static void main(String[] args) {
    Store lemonadeStand = new Store("Lemonade");
    lemonadeStand.advertise();
  }
}

}