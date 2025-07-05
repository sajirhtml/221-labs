import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class task1 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder S = new StringBuilder();

        int T = Integer.parseInt(B.readLine());
        while(T-- > 0) {
            int N = Integer.parseInt(B.readLine());
            if((N & 1) == 1){
                S.append(N).append(" is an Odd number.\n");
            }
            else{
                S.append(N).append(" is an Even number.\n");
            }
        }
        System.out.print(S);
    }
}