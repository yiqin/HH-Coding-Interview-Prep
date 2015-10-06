public class Solution {
    public static int numDecodings(String s) {

        int letters[] = new int[s.length()];
        for(int i = 0; i < letters.length; i++) {
            letters[i] = Integer.valueOf(s.substring(i, i+1));
        }

        int results[] = new int[letters.length];

        if (letters.length == 0) {
            return 0;
        }

        results[0] = 1;

        if (letters.length == 1) {
            return results[0];
        }

        if (letters[1] <= 6 && letters[0] <= 2) {
            results[1] = 2;
        } else {
            results[1] = 1;
        }

        if (letters.length == 2) {
            return results[1];
        }

        for(int i=2; i< results.length; i++) {

            int num1 = letters[i];
            int num2 = letters[i-1];

            int tempSum = num1+num2*10;
            if (tempSum <= 26) {
                results[i] = results[i-2]+results[i-1];
            } else {
                results[i] = results[i-2];
            }
        }

        return results[results.length-1];

    }
}