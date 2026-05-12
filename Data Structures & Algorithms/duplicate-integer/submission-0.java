class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> isDupe = new HashSet<Integer>();
        for(int i = 0; i  < nums.length; i++) {
            if(isDupe.contains(nums[i])) {
                return true;
            } else {
                isDupe.add(nums[i]);
            }
        }
        return false;
    }
}