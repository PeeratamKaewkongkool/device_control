public class Guitar extends MusicalInstrument implements Tunable {

    public Guitar(String name) {
        super(name, "String Instrument"); // เรียกใช้ Constructor ของ Superclass
    }

    @Override
    public void playSound() {
        System.out.println("Sound: Strum Strum~");
    }

    @Override
    public void performAction() {
        System.out.println("Action: Guitarist is plucking the strings.");
    }

    @Override
    public void tune() {
        System.out.println("Action: Adjusting guitar pegs to pitch standard E-A-D-G-B-E.");
    }
}