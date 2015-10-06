public static List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> results = new ArrayList<List<Integer>>();

    List<Integer> emptySubset = new ArrayList<Integer>();
    results.add(emptySubset);

    if(nums.length == 0) {
        return results;
    }

    Arrays.sort(nums);

    // init used Array
    boolean[] used = new boolean[nums.length];
    for(int i = 0; i < used.length; i++) {
        used[i] = false;
    }

    recursive(nums, used, new ArrayList<Integer>(), results, nums[0]-1);

    System.out.println(results);
    return results;
}


public static void recursive(int[] nums, boolean[] used, List<Integer> items, List<List<Integer>> results, int currentValue) {

    for(int i = 0; i < nums.length; i++) {

        if(!used[i] && nums[i] > currentValue) {

            used[i] = true;

            items.add(nums[i]);

            // Value typed....
            List<Integer> copyItems = new ArrayList<Integer>(items);
            results.add(copyItems);

            System.out.println("Result: "+results);

            recursive(nums, used, items, results, currentValue);

            currentValue = items.get(items.size()-1);
            items.remove(items.size()-1);

            used[i] = false;

        }

    }

}
