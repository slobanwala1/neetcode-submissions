# heap method
"""
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # example input: [1,2,2,3,3,3], k = 2
        # counter will be {3:3, 2:2, 1:1}
        counter = Counter(nums)
        heap = []

        for key, val  in counter.items():
            # Were adding in descending order, so we pop the lowest value when we hit
            # k amount of entries in heap. That way we get the most frequent(the greatest occurence pairs)
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
                
        # return the int values not occurences which is the second value in the pairs so 
        # traverse the heap and build and return it.
        return [h[1] for h in heap]

        # Time: O(n * log(k)), Space: O(n)
"""
# bucketsort method
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        # if inputs [1, 2, 3] buckets will be [0, 0, 0, 0]
        buckets = [0] * (n+1) 

        for num, freq in counter.items():
            if buckets[freq] == 0:
                # i.e if counter val is [2,2] then buckets is [0, 0, [2], 0]
                buckets[freq] = [num]
            else:
                # if another number has that freq we add/append to it not set/= it.
                # i.e if vals were [2,2], [3,2] then [0, 0, [2,3], 0]
                buckets[freq].append(num) 

        ret = []
        for i in range(n, -1, -1): # max size of list, last value
            # Go thru and grab the values not frequences thats why were going highest down.
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret


