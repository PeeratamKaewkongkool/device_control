public class Drum extends MusicalInstrument {

    public Drum(String name) {
        super(name, "Percussion Instrument");
    }

    @Override
    public void playSound() {
        System.out.println("Sound: Boom Boom Tap!");
    }

    @Override
    public void performAction() {
        System.out.println("Action: Drummer is hitting the drumhead with drumsticks.");
    }
}