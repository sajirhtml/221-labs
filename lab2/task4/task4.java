package task4;
import java.io.*;
import java.util.*;

public class task4 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        int N = Integer.parseInt(B.readLine());
        String[] arr1 = B.readLine().split(" ");
        int[] n = new int[N];
        int M = Integer.parseInt(B.readLine());
        String[] arr2 = B.readLine().split(" ");
        int[] m = new int[M];
        int p1 = 0, p2 = 0;
        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < N; i++) n[i] = Integer.parseInt(arr1[i]);
        for (int i = 0; i < M; i++) m[i] = Integer.parseInt(arr2[i]);

        while (true) {
            if (p1 >= N || p2 >= M) break;

            if (n[p1] > m[p2]) {
                ans.add(m[p2]);
                p2++;
            } 
            else if (n[p1] < m[p2]) {
                ans.add(n[p1]);
                p1++;
            } 
            else {
                ans.add(n[p1]);
                p1++;
                p2++;
            }
        }

        while (p1 < N) {
            ans.add(n[p1]);
            p1++;
        }

        while (p2 < M) {
            ans.add(m[p2]);
            p2++;
        }

        for (int num : ans) {
            P.print(num + " ");
        }
        P.println();
        P.flush();
    }
}