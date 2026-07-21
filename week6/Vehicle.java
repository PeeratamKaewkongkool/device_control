package week6;

public class Vehicle {
    protected String brand;

    public Vehicle(String brand){
        this.brand = brand;
    }

    public void startEngine(){
        System.out.print(":Engine Startted");
    }

    public void stopEndgine(){
        System.out.print(":Engine Stopped");
    }
}
