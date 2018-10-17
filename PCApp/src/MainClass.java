import File.FileTransfer;
import MouseKeyboard.MouseKeyboardControl;
import Network.Connection;
import Network.NetworkAPI;

import java.awt.*;
import java.io.IOException;

import static java.lang.System.exit;

public class MainClass {
    private static final byte DISCONNECT = 0;
    private static final byte FILESEND = 1;
    private static final byte MOUSE_MOVE = 2;

    private static Connection connection;
    private static MouseKeyboardControl mouseKeyboardControl;
    public static void main(String[] args) {
        final int PORT = 9999;
        Byte data = 100;
        NetworkAPI.initialize(PORT);
        Robot robot;
        try {
            robot = new Robot();
            mouseKeyboardControl = new MouseKeyboardControl(robot);
        } catch (AWTException e) {
            e.printStackTrace();
            exit(0);
        }
        while(true) {
            connection = NetworkAPI.connect();
            if(connection == null) {
                continue;
            }
            FileTransfer fileTransfer = new FileTransfer();
            /*try {
                fileTransfer.getSize(connection);
            } catch (IOException e) {
                e.printStackTrace();
            }*/
            do {
                data = connection.recieveByte();
                if(data == null)
                    continue;
                System.out.println(data);
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
            }while(data != DISCONNECT);
            NetworkAPI.disconnect(connection);
            System.out.println("Disconnected");
        }
    }
}
