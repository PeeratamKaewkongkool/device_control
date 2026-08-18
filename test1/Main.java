public class Main {
    public static void main(String[] args) {
        // สร้าง Array ของ Abstract Class เพื่อแสดงผล Polymorphism
        MusicalInstrument[] band = new MusicalInstrument[3];
        band[0] = new Guitar("Fender Stratocaster");
        band[1] = new Piano("Grand Piano");
        band[2] = new Drum("Pearl Drum Set");

        System.out.println("=== MUSICAL INSTRUMENT CONCERT ===\n");

        for (MusicalInstrument instrument : band) {
            // Polymorphism: เรียกใช้ method เดียวกัน แต่ผลลัพธ์ต่างกันตามชนิด Object
            instrument.displayDetails();
            instrument.playSound();
            instrument.performAction();

            // ตรวจสอบการใช้งาน Interface
            if (instrument instanceof Tunable) {
                ((Tunable) instrument).tune();
            } else {
                System.out.println("Tuning: This instrument does not require manual string tuning.");
            }

            System.out.println("-----------------------------------");
        }
    }
}