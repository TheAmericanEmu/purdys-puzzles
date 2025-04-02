import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;
import java.math.BigInteger;


public class Solver
{
        //o calculate all common divisors 
        // of two given numbers 
        // a, b --> input integer numbers 
        static int commDiv(BigInteger a, BigInteger b) 
        { 
            // find gcd of a, b 
            BigInteger n = a.gcd(b); 
    
            // Count divisors of n. 
            int result = 0; 
            for (BigInteger i = new BigInteger("1"); i.compareTo(n.sqrt())<1; i.add(new BigInteger("1"))) { 
                // if 'i' is factor of n 
                //System.out.println(i);
                if (n.mod(i).equals(new BigInteger("0"))) { 
                    // check if divisors are equal 
                    if (n.divide(i).equals(i)) 
                        result += 1; 
                    else
                        result += 2; 
                } 
            } 
            return result; 
        } 
 
        public static BigInteger convertArrayToInt(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be null or empty");
        }

        StringBuilder sb = new StringBuilder();
        for (int num : arr) {
            sb.append(num);
        }

        try {
            return new BigInteger(sb.toString());
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
                // System.out.print(num);

            }
            
            // System.out.println("-------------------");
            // System.out.println(convertArrayToInt(row));
    
        }

        //for(int i3=100;i3<1000;i3++){
            
        for(int row=0;row<ints.length;row++){
            BigInteger a = convertArrayToInt(ints[row]);
            //System.out.println(newLcm);
            for(int row2=0;row2<ints.length;row2++){
                BigInteger b = convertArrayToInt(ints[row2]);
                int newLcm=commDiv(a,b);
                //System.out.println(newLcm);
                if(true){
                    workingInts.add(newLcm);
                    //System.out.println(":"+newLcm);
                }
            }
        }
        //}
        for(Integer num: workingInts){
            System.out.println(num);
        }
    }
}
