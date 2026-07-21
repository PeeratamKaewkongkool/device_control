package week6;


public class Truck  extends Vehicle{
     public Truck(String brand){
      super(brand);
    }
    
    @Override
      public void startEngine() {
        System.out.println(brand + " : Truck Started");

      }

      public void carryCargo() {
        System.out.println(brand + " : ต่อพ่วงหลัง บรรทุกได้ 18 ตัน");
    }


}


