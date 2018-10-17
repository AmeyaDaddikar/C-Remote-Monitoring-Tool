package Network;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public final class NetworkAPI {
    public static ServerSocket serverSocket;

    private NetworkAPI(){}

    public static boolean initialize(int port) {
        try {
            serverSocket = new ServerSocket(port);
            System.out.println("Listening\n");
            return true;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to start server socket");
            return false;
        }
    }
    public static Connection connect() {
        try {
            Socket clientSocket = serverSocket.accept();
            Connection connection = new Connection(clientSocket);
            System.out.println("Connected\n");
            return connection;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to connect to client");
            return null;
        }
    }
    public static boolean disconnect(Connection connection) {
        try {
            connection.destroy();
            return true;
        } catch (IOException ie) {
            ie.printStackTrace();
            System.out.println("Unable to close connection or streams");
            return false;
        }
    }
}
