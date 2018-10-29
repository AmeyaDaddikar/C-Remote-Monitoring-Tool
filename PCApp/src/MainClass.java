import File.FileTransfer;
import MouseKeyboard.MouseKeyboardControl;
import Network.Connection;
import Network.NetworkAPI;

import java.awt.*;

class ThreadClass extends Thread {
    Connection connection;
    private static final byte DISCONNECT = 0;
    private static final byte FILESEND = 1;
    private static final byte MOUSE_MOVE = 2;
    private static final byte VIDEO = 3;
    private MouseKeyboardControl mouseKeyboardControl;

    public ThreadClass(Connection connection, Robot robot) {
        this.connection = connection;
        mouseKeyboardControl = new MouseKeyboardControl(robot);
    }

    @Override
    public void run() {
        super.run();
        FileTransfer fileTransfer = new FileTransfer();
        Byte data = 100;
        do {
            data = connection.recieveByte();
            if(data == null)
                continue;
            switch (data) {
                case FILESEND:
                    System.out.println("Sending file");
                    fileTransfer.sendFile(connection);
                    break;
                case MOUSE_MOVE:
                    mouseKeyboardControl.mouseMove(connection);
                    break;
                case DISCONNECT:
                    break;
                default:
                    mouseKeyboardControl.keyInput(data);
            }
        }while(DISCONNECT != data);
    }
}
public class MainClass {

    private static final byte DISCONNECT = 0;
    private static final byte FILESEND = 1;
    private static final byte MOUSE_MOVE = 2;
    private static final byte VIDEO = 3;
    private static final byte KEYBOARD = 4;
    private static Connection[] connection;
    public static void main(String[] args) throws InterruptedException {
        final int PORT = 9999;
        NetworkAPI.initialize(PORT);
        Robot robot = null;
        try {
            robot = new Robot();
        } catch (AWTException e) {
            e.printStackTrace();
            System.exit(0);
        }
        while(true) {
            connection = NetworkAPI.connect();
            if(connection == null) {
                continue;
            }
            ThreadClass[] threadClasses = new ThreadClass[4];
            for(byte i = 0; i < 4; i++)
            {
                threadClasses[i] = new ThreadClass(connection[i], robot);
            }
            for(ThreadClass threadClass: threadClasses)
                threadClass.start();
            for(ThreadClass threadClass: threadClasses)
                threadClass.join();
            /*try {
                fileTransfer.getSize(connection);
            } catch (IOException e) {
                e.printStackTrace();
            }*/
            NetworkAPI.disconnect(connection);
            System.out.println("Disconnected");
        }
    }
}
