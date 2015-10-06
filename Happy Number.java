public static boolean isHappy(int n) {

    if (n==1) {
        return true;
    }

    HashSet<Integer> set = new HashSet<Integer>();
    return checkHappyNumer(n, set);

}

public static boolean checkHappyNumer(int n, HashSet<Integer> set) {
    int sum = 0;

    while(n >= 10) {
        int remainder = n%10;
        sum = sum + remainder*remainder;
        n = n/10;
    }
    sum = sum + n*n;

    System.out.println(sum);

    if(sum == 1) {
        return true;
    } else {

        if (set.contains(sum)) {
            return false;
        }

        set.add(sum);
        return checkHappyNumer(sum, set);
    }

}
