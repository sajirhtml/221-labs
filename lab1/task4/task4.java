import java.io.*;
public class task4{
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter P = new PrintWriter(System.out);
        int T = Integer.parseInt(B.readLine());
        
        while(T-->0){
            boolean flag = true;
            int N = Integer.parseInt(B.readLine());
            String[] arr = B.readLine().split(" ");
            for(int i = 0; i < N-1; i++){
                if(Integer.parseInt(arr[i]) > Integer.parseInt(arr[i+1])){
                    P.println("NO");
                    flag = false;
                    break;
                }
            }
            if(flag) P.println("YES");
        }
        P.flush();
    }
}