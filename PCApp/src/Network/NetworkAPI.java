package Network;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public final class NetworkAPI {
    public static ServerSocket serverSocket, videoSocket, mouseSocket, keySocket;

    private NetworkAPI(){}

    public static boolean initialize(int port) {
        try {
            serverSocket = new ServerSocket(port);
            videoSocket = new ServerSocket(port + 1);
            mouseSocket = new ServerSocket(port + 2);
            keySocket = new ServerSocket(port + 3);
            System.out.println("Listening\n");
            return true;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to start server socket");
            return false;
        }
    }
    public static Connection[] connect() {
        try {
            Socket sock1 = serverSocket.accept();
            Socket sock2 = videoSocket.accept();
            Socket sock3 = mouseSocket.accept();
            Socket sock4 = keySocket.accept();
            Connection[] connection = new Connection[4];
            connection[0] = new Connection(sock1);
            connection[1] = new Connection(sock2);
            connection[2] = new Connection(sock3);
            connection[3] = new Connection(sock4);
            System.out.println("Connected\n");
            return connection;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to connect to client");
            return null;
        }
    }
    public static boolean disconnect(Connection[] connections) {
        try {
            for(Connection connection : connections)
                connection.destroy();
            return true;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to close connection or streams");
            return false;
        }
    }
}
