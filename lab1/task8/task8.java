package task8;
// import java.io.*;
// import java.util.Arrays;

// public class task8 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader( new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         int N = Integer.parseInt(B.readLine());
//         String[] trains = new String[N];

//         for(int i=0; i<N; i++){
//             trains[i] = B.readLine();
//         }

//         Arrays.sort(arr, (s1, s2) -> {
//             String[] p1 = s1.split(" ");
//             String[] p2 = s2.split(" ");

//         };

        

//         for(String s: trains){
//             P.println(s);
//         }
//         P.flush();
//     }
// }

import java.io.*;
import java.util.*;

public class task8{ 
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        int N = Integer.parseInt(B.readLine());
        String[] trains = new String[N];

        for (int i = 0; i < N; i++) {
            trains[i] = B.readLine();
        }

        Arrays.sort(trains, (s1, s2) -> {
            String n1 = s1.split(" ")[0];
            String n2 = s2.split(" ")[0];
            int cmp = n1.compareTo(n2);
            if (cmp != 0) return cmp;

            String t1 = s1.substring(s1.lastIndexOf(" ") + 1);
            String t2 = s2.substring(s2.lastIndexOf(" ") + 1);

            int min1 = Integer.parseInt(t1.split(":")[0]) * 60 + Integer.parseInt(t1.split(":")[1]);
            int min2 = Integer.parseInt(t2.split(":")[0]) * 60 + Integer.parseInt(t2.split(":")[1]);

            return Integer.compare(min2, min1);
        });

        for (String train : trains) {
            P.println(train);
        }
        P.flush();
    }
}
