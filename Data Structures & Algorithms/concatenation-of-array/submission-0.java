class Solution {
    public int[] getConcatenation(int[] nums) {
        int strLength = nums.length*2;
        int[] ans = new int[strLength];
        int j = 0;
        for(int i = 0; i < strLength; i++) {
            if(j < nums.length) {
                ans[i] = nums[j];
                j++;
            } 
            if(j == nums.length) {
                j = 0;
            }
        }
        return ans;
    }
}