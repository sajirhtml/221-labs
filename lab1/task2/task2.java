package task2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class task2 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder S = new StringBuilder();

        int T = Integer.parseInt(B.readLine());
        while (T-- > 0){
            String[] input = B.readLine().split(" ");
            double x = Double.parseDouble(input[1]);
            double y = Double.parseDouble(input[3]);
            String op = input[2];
            double result = 0;

            switch (op) {
                case "+":
                    result = x + y;
                    break;
                case "-":
                    result = x - y;
                    break;
                case "*":
                    result = x * y;
                    break;
                case "/":
                    result = x / y;
                    break;
            }
            S.append(String.format("%.6f", result)).append('\n');
        }
        System.out.print(S);
    }
}