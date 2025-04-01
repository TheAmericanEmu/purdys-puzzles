import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;


public class MyProgram
{

        public static int convertArrayToInt(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be null or empty");
        }

        StringBuilder sb = new StringBuilder();
        for (int num : arr) {
            sb.append(num);
        }

        try {
            return Integer.parseInt(sb.toString());
        } catch (NumberFormatException e) {
             throw new NumberFormatException("Could not parse the combined string to an integer: " + sb.toString());
        }
    }

    public static void main(String[] args) throws Exception{
        int[][] ints = new int[100][100];
        try {
            File file = new File("april25_puzzle.txt");
            Scanner input = new Scanner(file);
            int count=0;
            while(input.hasNextLine()){
                String line =input.nextLine();
                for(int i=0;i<=line.length()-1;i++){
                    ints[count][i]=(Integer.valueOf(line.substring(i,i+1)));
                }
                count++;
            }

        } catch (Exception e) {
            System.out.println(e);
        }
        ArrayList<Integer> workingInts= new ArrayList<Integer>();
        for(int[] row: ints){
            for(int num: row){
                System.out.print(num);

            }
            
            System.out.println("-------------------");
            System.out.println(convertArrayToInt(row));
    
        }

        for(int i3=100;i3<201;i3++){
            for(int row=0;row<ints.length;row++){
                
                if(convertArrayToInt(ints[row])%i3==0){
                    workingInts.add(i3);
                }
            }
        }
        for(int num: workingInts){
            System.out.println(num);
        }
    }
}
