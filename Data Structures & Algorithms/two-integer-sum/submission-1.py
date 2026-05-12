class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # since we know i != j we will use a set or hash table
        # We also know its a pair so cannot be a tuple or greater
        seen = {};
        for i, num in enumerate(nums):
            # total - the current index value
            complement = target - num
            print("complement:", complement)
            print("seen 1:", seen)
            # if the leftover sum is in our seen hash table we have our pair
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            print("seen 2:", seen)
        return []



        