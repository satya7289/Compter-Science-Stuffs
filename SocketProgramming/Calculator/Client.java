import java.net.*;
import java.io.*;
import java.util.*;

public class Client
{
    public static void main(String[] args) {
        try {
            Socket sock = new Socket("127.0.0.1",6013);
            var inServer = new Scanner(sock.getInputStream());
            var outServer = new PrintWriter(sock.getOutputStream(),true);
            var input = new Scanner(System.in);
            var print = new PrintWriter(System.out,true);
            print.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            print.println("\t Calculator using Socket Programming using multiple thread.\n");
            print.println("Operation you can do by the following methods.");
            print.println("Enter the S.No for the following operation.");
            print.print(" 1.Addtion\n 2.Substraction\n 3.Multiplication\n 4.Division\n 5.Square\n 6.Power\n 7.Square Root\n 8.Log followed by a and b i.e Log(a,b)\n 9.Answer, followed by which operation\n 10.Exit\n");
            print.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

            int operation=0;
            while(input.hasNextInt())
            {
                int choice = (int)input.nextDouble();
                if(choice==10){ print.println("Good Bye.."); break;}
                outServer.println(choice);
                print.println(++operation + " " +  inServer.nextLine());
                
            }
          
         
            sock.close();
        }
        catch (IOException ioe) {
        System.err.println(ioe);
        }
    }
}