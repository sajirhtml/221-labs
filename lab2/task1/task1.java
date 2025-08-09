import java.io.*;
public class task1{
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        String[] arr1 = B.readLine().split(" ");
        int N = Integer.parseInt(arr1[0]);
        int S = Integer.parseInt(arr1[1]);
        String[] arr2 = B.readLine().split(" ");
        int l = 0;
        int r = N-1;

        while(l<r){
            int lf = Integer.parseInt(arr2[l]);
            int ri = Integer.parseInt(arr2[r]);
            if(lf+ri == S){
                P.print((l+1) + " " + (r+1));
                P.flush();
                return;
            }
            else if(lf+ri < S){
                l++;
            }
            else{
                r--;
            }
        }
        P.print(-1);
        P.flush();
    }
}