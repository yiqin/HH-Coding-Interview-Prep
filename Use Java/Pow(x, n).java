
    public static double myPow(double x, int n) {

        if(n > 0) {
            return Pow(x, n);
        } else {
            return 1/Pow(x, -n);
        }

    }

    public static double Pow(double x, int n) {

        if(n == 0) {
            return 1;
        }

        if(n == 1) {
            return x;
        }

        int a = n/2;
        int b = n%2;

        return myPow(x*x, a)*myPow(x, b);
    }