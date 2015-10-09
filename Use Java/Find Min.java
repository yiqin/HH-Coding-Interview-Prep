public static void main(String[] args) {
// write your code here

// 4, 5, 6, 7, -1, 1, 2, 3
    int[] nums = new int[]{1, 2, 3};
    System.out.println(findMin(nums));

}

public static int findMin(int[] nums) {

    int result;

    if(nums.length == 0) {
        return 0;
    }

    int l = 0;
    int r = nums.length-1;

    if(nums[l] < nums[r]) {
        return nums[0];
    }


    while(true){

        int mid = (l+r)/2;

        // System.out.println(mid);

        if (l == r) {

//                // System.out.println(l);
//                if(l-1>=0){
//                    if (nums[l-1] < nums[l]){
//                        System.out.println("....");
//                        return nums[l-1];
//                    }
//                }

            return nums[l];
        }


        if (nums[mid] > nums[mid+1]) {

            result = nums[mid+1];
            System.out.println(result);
            return result;

        }
        else {

            if (nums[mid] > nums[l]) {
                l = mid;
            } else if (nums[mid] < nums[r]) {
                r = mid;
            }

        }
    }
}