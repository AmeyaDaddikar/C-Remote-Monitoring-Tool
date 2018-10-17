package File;

import Network.Connection;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileTransfer {
    private byte[] size;
    private byte[] contents;
    private byte[] full_contents;
    private int bytes, act_size, total_size, rem_size;
    private byte temp;

    public void getSize(Connection connection) throws IOException {
        size = new byte[4];
        contents = new byte[1024];
        if(connection.recieveBytes(size, size.length) > -1) {
            for(int i = 0; i < 4; i++) {
                System.out.println(size[i]);
            }
            for(int i = 0; i < 2; i++) {
                temp = size[i];
                size[i] = size[3 - i];
                size[3 - i] = temp;
            }
            for(int i = 0; i < 4; i++) {
                System.out.println(size[i]);
            }
            act_size = ByteBuffer.wrap(size).asIntBuffer().get();
            full_contents = new byte[act_size];
            System.out.println(act_size);
            total_size = 0;
            while(true) {
                rem_size = contents.length < (act_size - total_size) ? contents.length : (act_size - total_size);
                if(rem_size <= 0) break;
                bytes = connection.recieveBytes(contents, rem_size);
                if(bytes < 0) break;
                System.out.println("Rem size " + rem_size);
                System.out.println("Act rem size " + (act_size - total_size));
                System.out.println("Total Size " + total_size);
                System.out.println("Bytes " + bytes);
                System.arraycopy(contents, 0, full_contents, total_size, bytes);
                total_size += bytes;
            }
            BufferedImage image = ImageIO.read(new ByteArrayInputStream(full_contents));
            ImageIO.write(image, "jpg", new File("/home/vineet/Temp.jpeg"));
        }
        System.out.println(size.toString());
    }

    public void sendFile(Connection connection) {
        Integer file_name_size = connection.recieveInt();
        if(file_name_size == null)
            return;
        byte[] file_name = new byte[file_name_size];
        String act_name = null;
        if(connection.recieveBytes(file_name, file_name_size) > -1) {
            act_name = new String(file_name);
        }
        Path home = Paths.get(System.getProperty("user.home"));
        Path path = home.resolve(act_name);
        System.out.format("%s%n", path);
        try {
            byte[] contents = Files.readAllBytes(path);
            int file_size = contents.length;
            connection.sendInt(file_size);
            System.out.println("Sent size " + file_size);
            connection.sendBytes(contents);
            System.out.println("Sent file ");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
