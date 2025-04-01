import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;


public class Solver{
    public static void main(String[] args) throws Exception{
        try {
            int[][] ints = new int[100][100];
            File file = new File("april25_puzzle.txt");
            Scanner input = new Scanner(file);
            int count=0;
            while(input.hasNextLine()){
                String line =input.nextLine();
                for(int i=0;i<line.length()-1;i++){
                    ints[count][i]=(Integer.numberOf(line.substring(i,i+1)));
                }
                count++;
            }
            System.out.println(ints[0].length);
        } catch (Exception e) {
            System.out.println(e);
        }

    }
}