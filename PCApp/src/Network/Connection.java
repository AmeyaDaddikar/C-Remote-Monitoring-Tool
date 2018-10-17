package Network;

import java.io.*;
import java.net.Socket;
import java.nio.ByteBuffer;

public final class Connection {
    private Socket socket;
    private InputStream inputStream;
    private OutputStream outputStream;

    Connection(Socket socket) throws IOException {
        this.socket = socket;
        this.inputStream = this.socket.getInputStream();
        this.outputStream = this.socket.getOutputStream();
    }

    public boolean sendByte(byte data) {
//        outputStream.println(data);
        return true;
    }

    public void sendBytes(byte[] bytes) {
        try {
            outputStream.write(bytes);
            outputStream.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Byte recieveByte() {
        byte[] bytes = new byte[4];
        Byte data = null;
        byte temp;
        if(this.recieveBytes(bytes, bytes.length) > -1) {
//            for(int i = 0; i < 4; i++) {
//                System.out.println(bytes[i]);
//            }
            for(int i = 0; i < 2; i++) {
                temp = bytes[i];
                bytes[i] = bytes[3 - i];
                bytes[3 - i] = temp;
            }
//            for(int i = 0; i < 4; i++) {
//                System.out.println(bytes[i]);
//            }
            data = (byte)ByteBuffer.wrap(bytes).asIntBuffer().get();
        }
        return data;
    }

    public void sendInt(int data) {
        byte[] bytes = new byte[4];
        ByteBuffer.wrap(bytes).putInt(data);
        sendBytes(bytes);
    }
    public Integer recieveInt() {
        byte[] bytes = new byte[4];
        Integer data = null;
        byte temp;
        if(this.recieveBytes(bytes, bytes.length) > -1) {
//            for(int i = 0; i < 4; i++) {
//                System.out.println(bytes[i]);
//            }
            for(int i = 0; i < 2; i++) {
                temp = bytes[i];
                bytes[i] = bytes[3 - i];
                bytes[3 - i] = temp;
            }
//            for(int i = 0; i < 4; i++) {
//                System.out.println(bytes[i]);
//            }
            data = ByteBuffer.wrap(bytes).asIntBuffer().get();
        }
        return data;
    }

    public int recieveBytes(byte[] bytes, int size) {
        try {
            int read = this.socket.getInputStream().read(bytes, 0, size);
            //System.out.println(read);
            return read;
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Couldn't write data");
            return -2;
        }
    }

    void destroy() throws IOException {
        inputStream.close();
        outputStream.close();
        socket.close();
    }
}

