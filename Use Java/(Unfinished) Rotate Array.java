public static void main(String[] args) {
	// write your code here

        int[] nums = new int[]{1, 2};

        rotate(nums, 2);
    }

    public static void rotate(int[] nums, int k) {

        if(nums.length==1) {
            return;
        }

        if(k > nums.length)
            k=k%nums.length;

        List<Integer> result = new ArrayList<Integer>();

        int j = nums.length-k-1;

        System.out.println(j);

        for(int i = j; i< nums.length; i++) {
            if (j < 0) {

            }else {
                result.add(nums[i]);
            }
        }
        for(int i = 0; i<j; i++) {
            result.add(nums[i]);
        }

        System.out.println(result);

        for(int i = 0; i<nums.length; i++) {
            nums[i]= result.get(i);
        }
    }