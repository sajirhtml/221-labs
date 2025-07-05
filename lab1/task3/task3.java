// package task3;
// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.io.IOException;

// public class task3 {

//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         StringBuilder S = new StringBuilder();
//         int T = Integer.parseInt(B.readLine());

//         while (T-- > 0) {
//             long N = Long.parseLong(B.readLine());
//             long res = N * (N + 1) / 2;
//             S.append(res).append('\n');

//         }
//         System.out.print(S);
//     }
// }


package task3;
import java.io.*;
public class task3 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        
        int T = Integer.parseInt(B.readLine());
        
        while (T-- > 0) {
            long n = Long.parseLong(B.readLine());
            P.println(n * (n + 1) / 2);
        }
        P.flush();
    }
}