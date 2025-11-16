package Server;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

//import java.awt.Robot;
//import java.awt.event.KeyEvent;

public class Server {
    public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/test", new TesztHndl());
        server.createContext("/hangfel", new HangPHndl());
        server.setExecutor(null);
        server.start();
        System.out.println("server 8000es porton vfut");
    }

    static class TesztHndl implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String response = "This is the response";
            System.out.println("test");
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }

    static class HangPHndl implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String valasz = "Hangfel";
            System.out.println(valasz);
            try {
                // Robot gombokNyomkodoja = new Robot();
                // gombokNyomkodoja.keyPress(KeyEvent.VK_VOLUME_UP);
                Thread.sleep(200);
            } catch (Exception e) {
                e.printStackTrace();
            }
            // Thread.sleep(200);
            t.sendResponseHeaders(200, valasz.length());
            OutputStream os = t.getResponseBody();
            os.write(valasz.getBytes());
            os.close();
        }
    }
}
