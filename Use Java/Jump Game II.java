public class Solution {
    public int jump(int[] nums) {
        
        if (nums.length == 0) {
            return 0;
        }

        int jumps[] = new int[nums.length];
        jumps[0] = 0;

        for(int i = 1; i < jumps.length; i++) {

            int minJumps = -1;
            for(int j = 0; j < i; j++) {

                int jumpLength = j + nums[j];
                
                if (jumpLength >= i) {
                    if (minJumps < 0) {
                        minJumps = jumps[j]+1;
                    } else {
                        minJumps = Math.min(minJumps, jumps[j]+1);
                    }
                }

            }
            jumps[i] = minJumps;
            
        }

        return jumps[jumps.length-1];
        
    }
}