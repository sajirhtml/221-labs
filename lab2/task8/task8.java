package task8;

import java.io.*;
public class task8 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        int T = Integer.parseInt(B.readLine());
        
        for (int i = 0; i < T; i++) {
            String[] input = B.readLine().split(" ");
            int k = Integer.parseInt(input[0]);
            int x = Integer.parseInt(input[1]);
            int ans = k + (k - 1) / (x - 1);
            P.println(ans);
        }
        P.flush();
    }
} 