public class Equals {
  	public static void main(String[] args){
      String line1 = "Nah nah nah nah nah nah nah nah nah yeah";
      String line2 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";
      String line3 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";

      System.out.println(line1.equals(line2));
      System.out.println(line2.equals(line3));

    }       
}


/*
 *With objects, such as Strings, we can’t use the primitive equality operator. 
 To test equality with objects, we use a built-in method called .equals(). 
 When comparing objects, make sure to always use .equals(). 
 == will work occasionally, but the reason why it sometimes works has to do with how objects are stored in memory. 
*/