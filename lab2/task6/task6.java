package task6;

import java.io.*;
import java.util.*;

public class task6 {
    public static void main(String[] args) throws IOException {
        BufferedReader B = new BufferedReader(new InputStreamReader(System.in));
        String[] nInput = B.readLine().split(" ");
        String[] mInput = B.readLine().split(" ");
        int[] m = new int[mInput.length];
        int[] n = new int[nInput.length];
        int p1 = 0, p2 = 0, max = 0;
        HashMap<Integer, Integer> freq = new HashMap<>();
        
        for (int i = 0; i < nInput.length; i++) n[i] = Integer.parseInt(nInput[i]);
        for (int i = 0; i < mInput.length; i++) m[i] = Integer.parseInt(mInput[i]);
        
        while (true) {
            if (p2 >= n[0]) break;
            
            freq.put(m[p2], freq.getOrDefault(m[p2], 0) + 1);
            
            while (freq.size() > n[1]) {
                freq.put(m[p1], freq.get(m[p1]) - 1);
                if (freq.get(m[p1]) == 0) {
                    freq.remove(m[p1]);
                }
                p1++;
            }
            
            max = Math.max(max, p2 - p1 + 1);
            p2++;
        }
        
        System.out.println(max > 0 ? max : 0);
    }
}