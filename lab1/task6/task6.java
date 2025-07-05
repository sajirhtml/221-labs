package task6;
import java.io.*;

public class task6 {
    ;public static void main(String[] args)throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        int N = Integer.parseInt(B.readLine());
        String[] arr = B.readLine().split(" ");
        String temp;

        boolean flag = true;
        while (flag){
            flag = false;
            for (int i = 0; i < N - 1; i++) {
                int a = Integer.parseInt(arr[i]);
                int b = Integer.parseInt(arr[i + 1]);
                if (a % 2 == b % 2 && a > b) {
                    temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    flag = true;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            P.print(arr[i] + " ");
        }
        P.println();
        P.flush();
    }
}
