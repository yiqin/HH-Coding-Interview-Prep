public static int minSubArrayLen(int s, int[] nums) {

    int minSizeStarting = -1;
    int minSizeEnding = -1;

    int currentStarting = 0;
    int currentEnding = 0;

    int sum = 0;

    for(int i = 0; i< nums.length; i++) {

        currentStarting = i;
        sum = sum+nums[i];

        while( sum >= s ) {

            // System.out.println(sum);

            // System.out.println(minSizeEnding);

            if(minSizeStarting == -1) {

                minSizeStarting = currentStarting;
                minSizeEnding = currentEnding;
            }

            if((minSizeStarting >= 0) && (currentStarting-currentEnding) <= (minSizeStarting-minSizeEnding)){
                minSizeStarting = currentStarting;
                minSizeEnding = currentEnding;

            }

            // update, shorten the length
            sum = sum - nums[currentEnding];
            currentEnding++;
        }
    }

    // System.out.println("############");
    // System.out.println(minSizeStarting);
    // System.out.println(minSizeEnding);

    if (minSizeEnding == -1) {
        return  0;
    }

    return minSizeStarting-minSizeEnding+1;
}
