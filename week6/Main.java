package week6;

public class Main {
    

    public static void main(String[] args) {
        Car v1 = new Car("BMW");
        Motorcycle v2 = new  Motorcycle("Yamaha");
        Truck v3 = new Truck("Benz");
       
        

        v1.startEngine();
        v2.startEngine();
        v2.fireEx();
        v3.startEngine();
        v1.turnLeft();
        v1.turnRight();
        v2.showDetails();
        v3.carryCargo();
        


        System.out.println("-----------------------");

        v2.stopEndgine();
        v1.stopEndgine();

    }
}
