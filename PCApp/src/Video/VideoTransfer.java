package Video;

import Network.Connection;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.TimerTask;
import javax.imageio.ImageIO;
import java.io.ByteArrayOutputStream;

public class VideoTransfer extends TimerTask {

    private Connection connection;
    private Robot robot;
    private Rectangle screenSize;

    public VideoTransfer(Connection connection){
        this.connection = connection;

        screenSize = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
        try {
            robot = new Robot();
        } catch(AWTException awtExp){
            robot = null;
        }
    }

    @Override
    public void run() {
        BufferedImage screenFrame = robot.createScreenCapture(screenSize);

        byte[] screenBytes;
        ByteArrayOutputStream screen_stream = new ByteArrayOutputStream();
        try {
            ImageIO.write(screenFrame, "jpg", screen_stream);
            screenBytes = screen_stream.toByteArray();

            connection.sendBytes(screenBytes);

        } catch(IOException ioe){
            System.out.println("Error Writing screen data to bytes");
        }
    }
}
