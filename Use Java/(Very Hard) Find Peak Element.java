public static int findPeakElement(int[] nums) {


    int left = 0;
    int right = nums.length-1;

    while(left < right) {

        int mid = (left+right)/2;

        // System.out.println("left " + left);
        // System.out.println("right" + right);

        // Find it.
        if( (mid == 0|| nums[mid] > nums[mid-1]) && (mid == nums.length-1 || nums[mid] > nums[mid+1])) {

            return mid;
        }

        // System.out.println("hello"+mid);

        if(nums[mid] < nums[mid+1]) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return left;

}
