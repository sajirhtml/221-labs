// package task2;
// import java.io.*;

// public class task2 {
//     public static void main(String[] args) throws IOException{
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         String[] arr1 = B.readLine().split(" ");
//         int N = Integer.parseInt(arr1[0]);
//         int M = Integer.parseInt(arr1[1]);
//         int K = Integer.parseInt(arr1[2]);
//         String[] arr2 = B.readLine().split(" ");
//         String[] arr3 = B.readLine().split(" ");
//         int sum = 0;
//         int i = 0;
//         int j = M-1;
//         int x = 0;
//         int y = 0;

//         // for(int i = 0; i<N; i++){
//         //     for(int j = 0; j<M; j++){
//         //         int a = Integer.parseInt(arr2[i]);
//         //         int b = Integer.parseInt(arr3[j]);
//         //         int temp = (a + b)-K;

//         //         if(sum==0)sum = temp;
//         //         if(sum>temp){
//         //             sum = temp;
//         //             P.print((i+1) + " " + (j+1));
//         //         }
//         //         if(a + b == K){
//         //             P.print((i+1) + " " + (j+1));
//         //             P.flush();
//         //             return;
//         //         }
//         //     }
//         // }
//         // P.flush();

//         while(i<N && j>=0){
//             int a = Integer.parseInt(arr2[i]);
//             int b = Integer.parseInt(arr3[j]);
//             int temp = ((a + b));

//             if(temp == K){
//                 P.print((i+1) + " " + (j+1));
//                 P.flush();
//                 return;
//             } 

//             else if(temp < K){
//                 i++;
//             } 

//             else{
//                 j--;
//             }

//             if(sum == 0 || sum > temp){
//                 sum = temp;
//                 x=i+1;
//                 y=j+1;
//             }
//         }
//         P.println(x + " " + y);
//         P.flush();
//     }
// }


// package task2;
// import java.io.*;

// public class task2 {
//     public static void main(String[] args) throws IOException{
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);
//         String[] arr1 = B.readLine().split(" ");
//         int N = Integer.parseInt(arr1[0]);
//         int M = Integer.parseInt(arr1[1]);
//         int K = Integer.parseInt(arr1[2]);
//         String[] arr2 = B.readLine().split(" ");
//         String[] arr3 = B.readLine().split(" ");
        
//         int i = 0;
//         int j = M - 1;
//         int I = 1, J = 1;
//         int flag = Integer.MAX_VALUE;

//         while(i < N && j >= 0){
//             int a = Integer.parseInt(arr2[i]);
//             int b = Integer.parseInt(arr3[j]);
//             int sum = a + b;
//             int diff = Math.abs(sum - K);
        
//             if(diff < flag){
//                 flag = diff;
//                 I = i + 1;  
//                 J = j + 1;  
//             }

//             if(sum == K){
//                 P.println((i + 1) + " " + (j + 1));
//                 P.flush();
//                 return;
//             }
            
//             if(sum < K) i++;
//             else j--;
            
//         }
        
//         P.println(I + " " + J);
//         P.flush();
//     }
// }

// package task2;
// import java.io.*;

// public class task2 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
//         PrintWriter P = new PrintWriter(System.out);

//         String[] arr1 = B.readLine().trim().split(" ");
//         int N = Integer.parseInt(arr1[0]);
//         int M = Integer.parseInt(arr1[1]);
//         int K = Integer.parseInt(arr1[2]);

//         String[] arr2 = B.readLine().trim().split(" ");
//         String[] arr3 = B.readLine().trim().split(" ");
//         if (arr2.length != N || arr3.length != M) throw new RuntimeException("Invalid array length");

//         int i = 0, j = M - 1;
//         int I = 1, J = 1;
//         long minDiff = Long.MAX_VALUE;

//         while (i < N && j >= 0) {
//             int a = Integer.parseInt(arr2[i]);
//             int b = Integer.parseInt(arr3[j]);
//             long sum = (long) a + b; 
//             long diff = Math.abs(sum - K); 

//             if (diff < minDiff) {
//                 minDiff = diff;
//                 I = i + 1;
//                 J = j + 1;
//             }

//             if (sum == K) {
//                 P.println(I + " " + J);
//                 P.flush();
//                 return;
//             }

//             if (sum < K) i++;
//             else j--;
//         }

//         P.println(I + " " + J);
//         P.flush();
//     }
// }