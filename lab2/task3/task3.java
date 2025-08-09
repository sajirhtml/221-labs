package task3;
// // import java.io.*;
// // import java.util.Map;

// // public class task3 {
// //     public static void main(String[] args) throws IOException {
// //         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
// //         PrintWriter P = new PrintWriter(System.out);
// //         String[] arr1 = B.readLine().split(" ");
// //         String[] arr2 = B.readLine().split(" ");     
        
// //         int n = Integer.parseInt(arr1[0]);
// //         int x = Integer.parseInt(arr1[1]);
// //         int[] arr = new int[n];
// //         for(int i = 0; i < n; i++) arr[i] = Integer.parseInt(arr2[i]);

// //         for(int i = 0; i < n; i++){
// //             int a = x - arr[i];

// //             Map<Integer, Integer> map = new java.util.HashMap<>();
// //             for(int j = i+1; j < n; j++){
// //                 int b = a - Integer.parseInt(arr2[j]);
// //                 if(map.containsKey(b)){
// //                     int k = map.get(b);
// //                     P.print((i + 1) + " " + (k+1) + " " + (j+1));
// //                     P.flush();
// //                     return;
// //                 }
// //                 map.put(Integer.parseInt(arr2[j]), j);
// //             }
// //         }
// //         P.print(-1);
// //         P.flush();
// //     }
// // }

// // import java.util.*;
// // public class task3{
    
// //     static class ValueIndex{
// //         int value;
// //         int index;
        
// //         ValueIndex(int value, int index){
// //             this.value = value;
// //             this.index = index;
// //         }
// //     }
    
// //     public static void main(String[] args){
// //         Scanner sc = new Scanner(System.in);
        
// //         int n = sc.nextInt();
// //         int x = sc.nextInt();
        
// //         ValueIndex[] arr = new ValueIndex[n];
// //         for (int i = 0; i < n; i++){
// //             arr[i] = new ValueIndex(sc.nextInt(), i + 1);
// //         }
        
// //         Arrays.sort(arr, (a, b) -> Integer.compare(a.value, b.value));
        
// //         for (int i = 0; i < n - 2; i++){
// //             int s1 = x - arr[i].value;
// //             int left = i + 1;
// //             int right = n - 1;
            
// //             while(left < right){
// //                 int sum = arr[left].value + arr[right].value;
                
// //                 if(sum == s1){
// //                     System.out.println(arr[i].index + " " + arr[left].index + " " + arr[right].index);
// //                     return;
// //                 }

// //                 else if(sum < s1) left++;
// //                 else right--;
// //             }
// //         }
// //         System.out.println(-1);
// //     }
// // }


// import java.io.*;

// import java.util.*;

// public class task3{

    

//     static class Pair {

//         int value;

//         int index;

        

//         Pair(int value, int index) {

//             this.value = value;

//             this.index = index;

//         }

//     }

    

//     public static void main(String[] args) throws IOException {

//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));

//         String[] firstLine = B.readLine().split(" ");

//         int n = Integer.parseInt(firstLine[0]);

//         int x = Integer.parseInt(firstLine[1]);

        

//         String[] secondLine = B.readLine().split(" ");

        

//         Pair[] paired = new Pair[n];

//         for (int i = 0; i < n; i++) {

//             paired[i] = new Pair(Integer.parseInt(secondLine[i]), i + 1);

//         }


//         Arrays.sort(paired, (a, b) -> Integer.compare(a.value, b.value));

        

//         int i = 0;

//         boolean found = false;

        

//         while (true) {

//             if (i >= n - 2) {

//                 break;

//             }

            

//             int s1 = x - paired[i].value;

//             int p1 = i + 1;

//             int p2 = n - 1;

            

//             while (true) {

//                 if (p1 >= p2) {

//                     break;

//                 }

                

//                 int total = paired[p1].value + paired[p2].value;

                

//                 if (total == s1) {

//                     System.out.println(paired[i].index + " " + paired[p1].index + " " + paired[p2].index);

//                     found = true;

//                     break;

//                 } else if (total < s1) {

//                     p1++;

//                 } else {

//                     p2--;

//                 }

//             }

            

//             if (found) {

//                 break;

//             }

//             i++;

//         }

        

//         if (!found) {

//             System.out.println(-1);

//         }

//     }

// }

// import java.io.*;
// import java.util.*;

// public class ThreeSumWithIndices {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);

//         String[] arr1 = B.readLine().split(" ");
//         int n = Integer.parseInt(arr1[0]);
//         int x = Integer.parseInt(arr1[1]);

//         String[] arr2 = B.readLine().split(" ");
//         int[] a = new int[n];
//         Pair[] arr = new Pair[n];

//         for (int i = 0; i < n; i++) {
//             a[i] = Integer.parseInt(arr2[i]);
//             arr[i] = new Pair(a[i], i + 1);
//         }

//         Arrays.sort(arr, Comparator.comparingInt(p -> p.val));

//         for (int i = 0; i < n - 2; i++) {
//             int s1 = x - arr[i].val;
//             int l = i + 1;
//             int r = n - 1;

//             while (l < r) {
//                 int sum = arr[l].val + arr[r].val;
//                 if (sum == s1) {
//                     P.println(arr[i].idx + " " + arr[l].idx + " " + arr[r].idx);
//                     P.flush();
//                     return;
//                 } else if (sum < s1) {
//                     l++;
//                 } else {
//                     r--;
//                 }
//             }
//         }

//         P.println("-1");
//         P.flush();
//     }

//     static class Pair {
//         int val, idx;
//         Pair(int v, int i) {
//             val = v;
//             idx = i;
//         }
//     }
// }


import java.io.*;
import java.util.*;

public class task3 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        String[] arr1 = B.readLine().split(" ");
        String[] arr2 = B.readLine().split(" ");
        int n = Integer.parseInt(arr1[0]);
        int x = Integer.parseInt(arr1[1]);
        int[] a = new int[n];
        Pair[] arr = new Pair[n];

        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(arr2[i]);

        for (int i = 0; i < n; i++) arr[i] = new Pair(a[i], i + 1);

        Arrays.sort(arr, Comparator.comparingInt(p -> p.val));

        for (int i = 0; i < n; i++) {
            int s1 = x - arr[i].val;
            int l = 0, r = n - 1;

            while (l < r) {
                if (l == i) {
                    l++;
                    continue;
                }
                if(r == i) {
                    r--;
                    continue;
                }

                int sum = arr[l].val + arr[r].val;
                if (sum == s1) {
                    int e = arr[i].idx, f = arr[l].idx, g = arr[r].idx;
                    if (e != f && f != g && e != g) {
                        P.println(e + " " + f + " " + g);
                        P.flush();
                        return;
                    }
                    l++;
                } 
                else if (sum < s1) l++;
                else r--;
            }
        }

        P.println("-1");
        P.flush();
    }

    public static class Pair {
        int val, idx;
        Pair(int v, int i) {
            val = v;
            idx = i;
        }
    }
}
