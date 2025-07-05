package task7;

// import java.io.*;

// public class task7 {
//     public static void main(String[] args) throws IOException{
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         int N = Integer.parseInt(B.readLine());
//         String[] ids = B.readLine().split(" ");
//         String[] scores = B.readLine().split(" ");
//         int count = 0;

//         for(int i = 0; i<N-1; i++){
//             int min = i;
//             for(int j = i+1; j<N; j++){
//                 if(Integer.parseInt(scores[j]) > Integer.parseInt(scores[min])){
//                     min = j;
//                 }
//             }

//             if(min != i){
//                 String tempId = ids[i];
//                 String tempScore = scores[i];
//                 ids[i] = ids[min];
//                 scores[i] = scores[min];
//                 ids[min] = tempId;
//                 scores[min] = tempScore;
//                 count++;
//             }
//         }

//         P.print("Minimum count: " + count + "\n");
//         for(int i = 0; i < N; i++){
//             P.print("ID: " + ids[i] + " "+ "Mark: " + scores[i] + "\n");
//         }
//         P.flush();
//     }
// }


// package task7;
// import java.io.*;
// public class task7{
//     public static void main(String[] args) throws IOException{
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         int N = Integer.parseInt(B.readLine());
//         String[] ids = B.readLine().split(" ");
//         String[] scores = B.readLine().split(" ");
//         int count = 0;

//         for(int i = 0; i<N-1; i++){
//             int cS = Integer.parseInt(scores[i]);
//             String cId = ids[i];
//             int pos = i;

//             for(int j = i+1; j<N; j++){
//                 if(Integer.parseInt(scores[j]) < cS){
//                     pos++;
//                 }
//             }

//             if(pos == i){
//                 continue;
//             }

//             if(pos != i){
//                 String tempId = ids[pos];
//                 String tempS = scores[pos];
//                 ids[pos] = cId;
//                 scores[pos] = String.valueOf(cS);
//                 cId = tempId;
//                 cS = Integer.parseInt(tempS);
//                 count++;
//             }

//             while(cS == Integer.parseInt(scores[pos])){
//                 pos++;
//             }

//             while(pos !=i){
//                 pos = i;
//                 for(int k = i+1; k<N; k++){
//                     if(Integer.parseInt(scores[k]) < cS){
//                         pos++;
//                     }
//                 }
//             }

//             if (cS != Integer.parseInt(scores[pos])) {
//                     String tempId = ids[pos];
//                     String tempScore = scores[pos];
//                     ids[pos] = cId;
//                     scores[pos] = String.valueOf(cS);
//                     cId = tempId;
//                     cS = Integer.parseInt(tempScore);
//                     count++;
//                 }
//         }

//         P.print("Minimum count: " + count + "\n");
//         for(int i = 0; i < N; i++){
//             P.print("ID: " + ids[i] + " "+ "Mark: " + scores[i] + "\n");
//         }
//     }
// }

// package task7;
// import java.io.*;

// public class task7 {
//     public static void main(String[] args) throws IOException{
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         int N = Integer.parseInt(B.readLine());
//         int[] ids = new int[N];
//         int[] marks = new int[N];
//         String[] idSt = B.readLine().split(" ");
//         String[] markSt = B.readLine().split(" ");
//         int count = 0;

//         for(int i = 0; i < N; i++){
//             ids[i] = Integer.parseInt(idSt[i]);
//             marks[i] = Integer.parseInt(markSt[i]);
//         }

//         for(int cS = 0; cS < N - 1; cS++){
//             int cId = ids[cS];
//             int cMark = marks[cS];
//             int pos = cS;

//             for(int j = cS + 1; j < N; j++){
//                 if(chotoderAageDao(marks[j], ids[j], cMark, cId)) {
//                     pos++;
//                 }
//             }

//             if(pos == cS) continue;

//             while(pos < N && marks[pos] == cMark && ids[pos] == cId){
//                 pos++;
//             }

//             if(pos != cS){
//                 int tempM = marks[pos];
//                 int tempId = ids[pos];
//                 marks[pos] = cMark;
//                 ids[pos] = cId;
//                 cMark = tempM;
//                 cId = tempId;
//                 count++;
//             }

//             while(pos != cS){
//                 pos = cS;
//                 for (int j = cS + 1; j < N; j++) {
//                     if (chotoderAageDao(marks[j], ids[j], cMark, cId)){
//                         pos++;
//                     }
//                 }

//                 while(pos < N && marks[pos] == cMark && ids[pos] == cId){
//                     pos++;
//                 }

//                 if(cMark != marks[pos] || cId != ids[pos]){
//                     int tempM = marks[pos];
//                     int tempId = ids[pos];
//                     marks[pos] = cMark;
//                     ids[pos] = cId;
//                     cMark = tempM;
//                     cId = tempId;
//                     count++;
//                 }
//             }
//         }


//         P.println("Minimum swaps: " + count);
//         for(int i = 0; i < N; i++){
//             P.println("ID: " + ids[i] + " Mark: " + marks[i]);
//         }
//         P.flush();
//     }


//     private static boolean chotoderAageDao(int m1, int id1, int m2, int id2){
//         if (m1 > m2) return true;
//         if (m1 < m2) return false;
//         return id1 < id2;
//     }
// }

import java.io.*;
import java.util.*;

public class task7 {
    static class S {
        int id, m;
        S(int id, int m) {
            this.id = id;
            this.m = m;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter w = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(r.readLine());
        String[] idStr = r.readLine().split(" ");
        String[] mStr = r.readLine().split(" ");

        S[] a = new S[n];
        for (int i = 0; i < n; i++) {
            a[i] = new S(Integer.parseInt(idStr[i]), Integer.parseInt(mStr[i]));
        }

        S[] b = Arrays.copyOf(a, n);
        Arrays.sort(b, (x, y) -> {
            if (y.m != x.m) return y.m - x.m;
            return x.id - y.id;
        });

        Map<String, Integer> idx = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String key = b[i].id + "-" + b[i].m;
            idx.put(key, i);
        }

        int[] pos = new int[n];
        for (int i = 0; i < n; i++){
            String key = a[i].id + "-" + a[i].m;
            pos[i] = idx.get(key);
        }

        boolean[] vis = new boolean[n];
        int sw = 0;
        for (int i = 0; i < n; i++){
            if (vis[i] || pos[i] == i) continue;
            int c = 0, j = i;
            while (!vis[j]) {
                vis[j] = true;
                j = pos[j];
                c++;
            }
            sw += c - 1;
        }

        w.write("Minimum swaps: " + sw + "\n");
        for (S s : b) {
            w.write("ID: " + s.id + " Mark: " + s.m + "\n");
        }
        w.flush();
    }
}