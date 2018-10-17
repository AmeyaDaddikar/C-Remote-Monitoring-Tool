package MouseKeyboard;

import Network.Connection;

import java.awt.*;
import java.awt.event.KeyEvent;

public final class MouseKeyboardControl {
    Robot robot;

    public MouseKeyboardControl(Robot robot) {
        this.robot = robot;
    }

    public void mouseMove(Connection connection) {
        Integer x = connection.recieveInt();
        Integer y = connection.recieveInt();
        robot.mouseMove(x,y);
    }

    public void keyInput(byte data) {
//        char ch = (char) data;
//        System.out.println("Char " + ch);
        int key = KeyEvent.getExtendedKeyCodeForChar(data);
//        System.out.println("Int key " + ch);
//        System.out.println("A " + KeyEvent.VK_A);
        System.out.println("A " + KeyEvent.getExtendedKeyCodeForChar((byte)'A') + " a " + KeyEvent.getExtendedKeyCodeForChar((byte)'a'));
        if(Character.isUpperCase((char)data)) {
            doType(KeyEvent.VK_SHIFT, key);
        }
        else {
            doType(key);
        }
    }
    public void doType(int... keyCodes) {
        int length = keyCodes.length;
        for (int i = 0; i < length; i++) {
            robot.keyPress(keyCodes[i]);
        }
        robot.delay(10);
        for (int i = length - 1; i >= 0; i--) {
            robot.keyRelease(keyCodes[i]);
        }
    }
}
