import java.net.*;
import java.io.*;
import java.util.*;
import java.util.concurrent.Executors;
import java.lang.Math;

// 1.Addtion\n 2.Substraction\n 3.Multiplication\n 4.Division\n 5.Square\n 6.Power\n 7.Square Root\n 8.Log followed by a and b i.e Log(a,b)\n 9.Answer, followed by which operation\n 10.Exit\n
public class Server
{
    public static void main(String[] args) {
        try {
            ServerSocket sock = new ServerSocket(6013);
            System.out.println("Server is running on localPort " + "6013 " + new java.util.Date().toString());
            var pool = Executors.newFixedThreadPool(20); // 100 thread...
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
                List<Double> array = new ArrayList<>();
                var inClient  = new Scanner(socket.getInputStream());
                var outClient = new PrintWriter(socket.getOutputStream(),true);
                var input = new Scanner(System.in);
                var print = new PrintWriter(System.out,true);
                while(inClient.hasNextDouble()){
                    Double choice = inClient.nextDouble();
                    print.println(choice);
                    if(choice==1){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        Double ans = x+y;
                        outClient.println("Addition = " + ans);
                        array.add(ans);
                    }
                    if(choice==2){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        Double ans = x-y;
                        outClient.println("Substraction = " + ans);
                        array.add(ans);
                    }
                    if(choice==3){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        Double ans = x*y;
                        outClient.println("Multiplication = " + ans);
                        array.add(ans);
                    }
                    if(choice==4){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        if(y!=0){
                             Double ans = x/y;
                             outClient.println("Division = " + ans);
                             array.add(ans);
                        }
                        else
                         outClient.println("!! Error y can't be zero.");
                    }
                    if(choice==5){
                        Double x = inClient.nextDouble();
                        Double ans = x*x;
                        outClient.println("Sqaure = " + ans);
                        array.add(ans);
                    }
                    if(choice==6){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        Double ans = Math.pow(x,y);
                        outClient.println("Power = " + ans);
                        array.add(ans);
                    }
                    if(choice==7){
                        Double x = inClient.nextDouble();
                        Double ans = Math.sqrt(x);
                        outClient.println("Square Root = " + ans);
                        array.add(ans);
                    }
                    if(choice==8){
                        Double x = inClient.nextDouble();
                        Double y = inClient.nextDouble();
                        Double ans = Math.log(x)/Math.log(y);
                        outClient.println("Log = " + ans);
                        array.add(ans);
                    }
                     if(choice==9){
                        int x = (int)inClient.nextDouble();
                        Double ans = array.get(x-1);
                        outClient.println("Answer = " + ans);
                    }
                    
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