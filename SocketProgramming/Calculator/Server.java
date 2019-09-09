import java.net.*;
import java.io.*;
import java.util.*;
import java.util.concurrent.Executors;

// 1.Addtion\n 2.Substraction\n 3.Multiplication\n 4.Division\n 5.Square\n 6.Power\n 7.Square Root\n 8.Log followed by a and b i.e Log(a,b)\n 9.Answer, followed by which operation\n 10.Exit\n
public class Server
{
    public static void main(String[] args) {
        try {
            ServerSocket sock = new ServerSocket(6013);
            System.out.println("Server is running on localPort " + "6013 " + new java.util.Date().toString());
            var pool = Executors.newFixedThreadPool(20); // 100 thread...
            List<Double> array = new ArrayList<>();
            while (true) {
             pool.execute(new Calculation(sock.accept()));
            }
        }
        catch (IOException ioe) {
        System.err.println(ioe);
        }
    }

    private static class Calculation implements Runnable{
        private Socket socket;
        Calculation(Socket sock){
            this.socket = sock;
        }

        @Override
        public void run(){
            System.out.println("Client Connected " + socket);
            try{
                var inClient  = new Scanner(socket.getInputStream());
                var outClient = new PrintWriter(socket.getOutputStream(),true);
                var input = new Scanner(System.in);
                var print = new PrintWriter(System.out,true);
                while(inClient.hasNextDouble()){
                    Double choice = inClient.nextDouble();
                    print.println(choice);
                    print.println(this.add(2,5));
                    outClient.println("SATYA");
                }

            }
            catch (Exception e) {
                System.out.println("Error:" + socket);
            }
            finally {
                try {
                     socket.close(); 
                } 
                catch (IOException e) {}
                System.out.println("Closed: " + socket + "\n");
            }
        }
    }
}