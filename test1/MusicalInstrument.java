// Abstract Class หลักสำหรับเครื่องดนตรี
public abstract class MusicalInstrument {
    private String name;
    private String type;

    // Constructor
    public MusicalInstrument(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    // Abstract Methods
    public abstract void playSound();
    public abstract void performAction();

    // Concrete Method
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Type: " + type);
    }
}
