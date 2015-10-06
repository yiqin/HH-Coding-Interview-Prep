    public int firstMissingPositive(int[] nums) {
        
        boolean[] results = new boolean[nums.length+1];

        for(int i = 0; i < nums.length; i++) {

            if(nums[i] > 0) {
                if(nums[i] < results.length) {
                    results[nums[i]] = true;
                }

            }
        }

        // System.out.println(minPositive);

        // System.out.println(results);

        for (int i = 1; i < results.length; i++) {

            // System.out.println(results[i]);

            if(results[i] == false) {
                return i;
            }

            if(results[i] == true && i == results.length-1) {
                return i+1;
            }
        }

        return 1;
    }