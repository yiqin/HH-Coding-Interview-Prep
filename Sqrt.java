public static int mySqrt(int x) {

    int result = 0;

    for(int i = 0; i < x; i++) {
        if(i*i == x) {
            result = i;
            break;
        } else if (i*i > x) {
            result = i-1;
            break;
        }
    }

    return result;
}