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
//                     Break;
//                 }
//             }
//             if(flag) P.println("YES");
        
//     }
// }


// import java.io.*;
// public class task5 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         int N = Integer.parseInt(B.readLine());
//         String[] arrStr = B.readLine().split(" ");
//         int[] arr = new int[N];
//         boolean sorted = true;

//         for (int i = 0; i < N; i++) {
//             arr[i] = Integer.parseInt(arrStr[i]);
//         }
        
//         for (int i = 1; i < N; i++) {
//             if (arr[i - 1] > arr[i]) {
//                 sorted = false;
//                 break;
//             }
//         }
//         System.out.println(sorted ? "YES" : "NO");
//     }
// }


// import java.io.*;
// import java.util.*;

// public class task5{
//     public static void main(String[] args) throws IOException {

//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         int n = Integer.parseInt(br.readLine());
//         String[] input = br.readLine().split(" ");
//         int[] arr = new int[n];

//         for(int i = 0; i < n; i++){
//             arr[i] = Integer.parseInt(input[i]);
//         }

//         if(n <= 2){
//             System.out.println("YES");
//             return;
//         }
        
//         int eCount = (n + 1) / 2;
//         int oCount = n / 2;
//         int[] eElem = new int[eCount];
//         int[] oElem = new int[oCount];
//         int eIdx = 0, oIdx = 0;

//         for(int i = 0; i < n; i++){
//             if(i % 2 == 0){
//                 eElem[eIdx++] = arr[i];
//             } 
//             else{
//                 oElem[oIdx++] = arr[i];
//             }
//         }

//         Arrays.sort(eElem);
//         Arrays.sort(oElem);
//         Arrays.sort(arr);
//         eIdx = 0;
//         oIdx = 0;

//         for(int i = 0; i < n; i++){
//             int a = arr[i];
//             int b = (i % 2 == 0) ? eElem[eIdx++] : oElem[oIdx++];

//             if(a != b){
//                 System.out.println("NO");
//                 return;
//             }
//         }
//         System.out.println("YES");
//     }
// }

// import java.io.*;
// public class task5{ 
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         int n = Integer.parseInt(B.readLine());
//         String[] arr = B.readLine().split(" ");
//         int[] a = new int[n];

//         for (int i = 0; i < n; i++) {
//             a[i] = Integer.parseInt(arr[i]);
//         }

//         for (int j = 0; j < n; j++) {
//             for (int i = 0; i + 2 < n; i++) {
//                 if (a[i] > a[i + 2]) {
//                     int temp = a[i];
//                     a[i] = a[i + 2];
//                     a[i + 2] = temp;
//                 }
//             }
//         }

//         boolean flag = true;
//         for (int i = 0; i + 1 < n; i++) {
//             if (a[i] > a[i + 1]) {
//                 flag = false;
//                 break;
//             }
//         }

//         System.out.println(flag ? "YES" : "NO");
//     }
// }

// 300000
// import java.io.*;
// public class task5 { 
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         int n = Integer.parseInt(B.readLine());
//         String[] arr = B.readLine().split(" ");
//         int[] a = new int[n];

//         for (int i = 0; i < n; i++) {
//             a[i] = Integer.parseInt(arr[i]);
//         }

//         for (int loop = 0; loop < n; loop++) {
//             for (int i = 0; i + 2 < n; i++) {
//                 if (a[i] > a[i+1] || a[i+1] > a[i+2] || a[i] > a[i+2]) {
//                     int x = a[i], y = a[i+1], z = a[i+2];
//                     a[i] = z;
//                     a[i+1] = y;
//                     a[i+2] = x;
//                 }
//             }
//         }

//         boolean flag = true;
//         for (int i = 0; i + 1 < n; i++) {
//             if (a[i] > a[i + 1]) {
//                 flag = false;
//                 break;
//             }
//         }
//         System.out.println(flag ? "YES" : "NO");
//     }
// }

// import java.io.*;
// public class task5 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         int n = Integer.parseInt(B.readLine());
//         String[] arr = B.readLine().split(" ");
//         int[] a = new int[n];
//         for (int i = 0; i < n; i++) {
//             a[i] = Integer.parseInt(arr[i]);
//         }

//         int inv = 0;
//         for (int i = 0; i < n; i++) {
//             for (int j = i + 1; j < n; j++) {
//                 if (a[i] > a[j]) {
//                     inv++;
//                 }
//             }
//         }
//         System.out.println((inv % 2 == 0) ? "YES" : "NO");
//     }
// }


// import java.io.*;
// public class task5 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         int n = Integer.parseInt(B.readLine());
//         String[] input = B.readLine().split(" ");
//         int[] a = new int[n];
//         for(int i = 0; i < n; i++){
//             a[i] = Integer.parseInt(input[i]);
//         }

//         for(int i = 0; i <= n - 3; i++){
//             int minI = i;
//             for(int j = i + 1; j < n; j++){
//                 if(a[j] < a[minI]){
//                     minI = j;
//                 }
//             }

//             while(minI - i >= 2){
//                 reverse3(a, minI - 2);
//                 minI -= 2;
//             }

//             if(minI - i == 1){
//                 reverse3(a, i);
//                 reverse3(a, i);
//             }
//         }

//         if(a[n - 2] <= a[n - 1]){
//             System.out.println("YES");
//         } 
//         else{
//             System.out.println("NO");
//         }
//     }

//     static void reverse3(int[] a, int i){
//         int temp = a[i];
//         a[i] = a[i + 2];
//         a[i + 2] = temp;
//     }
// }


import java.io.*;
public class task5 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(B.readLine());
        String[] arr = B.readLine().split(" ");
        int[] a = new int[n];
        boolean cng = true;
        boolean flag = true;

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(arr[i]);
        }
        

        while (cng) {
            cng = false;
            for (int i = 0; i + 2 < n; i++) {
                if (a[i] > a[i+2]) {
                    int temp = a[i];
                    a[i] = a[i+2];
                    a[i+2] = temp;
                    cng = true;
                }
            }
        }
        
        
        for (int i = 0; i + 1 < n; i++) {
            if (a[i] > a[i + 1]) {
                flag = false;
                break;
            }
        }
        System.out.println(flag ? "YES" : "NO");
    }
}