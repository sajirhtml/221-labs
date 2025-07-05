// package task5;
// import java.io.*;

// public class task5 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         int N = Integer.parseInt(B.readLine());
//         String[] arr = B.readLine().split(" ");
//         boolean flag = true;

//         for(int i = 0; i < N-1; i++){
//             if(Integer.parseInt(arr[i]) > Integer.parseInt(arr[i+1])){
//                     P.println("NO");
//                     flag = false;
//                     break;
//                 }
//             }
//             if(flag) P.println("YES");
        
//     }
// }


import java.io.*;
import java.util.*;

public class task {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tokens = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tokens[i]);
        }
        if (n <= 2) {
            boolean sorted = true;
            for (int i = 1; i < n; i++) {
                if (arr[i - 1] > arr[i]) {
                    sorted = false;
                    break;
                }
            }
            System.out.println(sorted ? "YES" : "NO");
        } else {
            System.out.println("YES");
        }
    }
}
