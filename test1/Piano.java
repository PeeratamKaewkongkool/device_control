public class Piano extends MusicalInstrument implements Tunable {

    public Piano(String name) {
        super(name, "Keyboard Instrument");
    }

    @Override
    public void playSound() {
        System.out.println("Sound: Plink Plonk~");
    }

    @Override
    public void performAction() {
        System.out.println("Action: Pianist is pressing the weighted keys.");
    }

    @Override
    public void tune() {
        System.out.println("Action: Tightening piano strings with a tuning hammer.");
    }
}
