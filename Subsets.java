public static void main(String[] args) {
// write your code here

    int[] nums = new int[]{1, 2, 3};

    subsets(nums);
}

public static List<List<Integer>> subsets(int[] nums) {

    List<List<Integer>> results = new ArrayList<List<Integer>>();

    if(nums == null) {
        return null;
    }


    boolean[] used = new boolean[nums.length];
    for(int i = 0; i< used.length; i++) {
        used[i] = false;
    }

    List<Integer> emptyItems = new ArrayList<Integer>();
    results.add(emptyItems);
    getSubsets(nums, used, new ArrayList<Integer>(), results);

    // System.out.println(results);

    return results;
}

public static void getSubsets(int[] nums, boolean[] used, ArrayList<Integer> items, List<List<Integer>> results) {

    for(int i = 0; i < nums.length; i++) {

        if(!used[i]) {

            if((items.size() > 0 && items.get(items.size()-1) < nums[i]) || items.size() == 0 ) {

                items.add(nums[i]);
                used[i] = true;

                // System.out.println(items);


                results.add(new ArrayList<Integer>(items));

                // recursive...
                getSubsets(nums, used, items, results);

                items.remove(items.size() - 1);
                used[i] = false;
            }

        }
    }

}