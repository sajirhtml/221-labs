package task5;
import java.io.*;

public class task5 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        String[] arr1 = B.readLine().split(" ");
        String[] arr2 = B.readLine().split(" ");
        int[] m = new int[arr2.length];
        int[] n = new int[arr1.length];
        int a = 0 ,b = 0 ,sum = 0, max = 0;

        for (int i = 0; i < arr1.length; i++) n[i] = Integer.parseInt(arr1[i]);
        for (int i = 0; i < arr2.length; i++) m[i] = Integer.parseInt(arr2[i]);
        

        
        while (true) {
            if (b >= n[0]) break;
            
            sum += m[b];
            while (sum > n[1] && a <= b) {
                sum -= m[a];
                a++;
            }
            max = Math.max(max, b - a + 1);
            b++;
        }
        System.out.println(max > 0 ? max : 0);
    }
}
