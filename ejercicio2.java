import java.util.random.*;
public class ejercicio2 {



public static void main(String[] args) {
    
System.err.println("Hola Mundo");
  
   float costo = 800;
   float venta = 1500;
   float donacion = 2;

   float randon = demandaDiaria();
   System.out.println(randon);
 }
}


public static float demandaDiaria(){
   float d = (Math.random());
   return d;
}