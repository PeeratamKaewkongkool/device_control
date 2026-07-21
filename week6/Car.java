package week6;

public class Car extends Vehicle {

    public Car(String brand){
        super(brand);
    }
    
    @Override
    public void startEngine(){
        System.out.println(brand + ": Car Engine Started");
    }
    public void turnLeft() {
        System.out.println(brand + " : Turn Left");
    }

    public void turnRight() {
        System.out.println(brand + " : Turn Right");
    }
}






