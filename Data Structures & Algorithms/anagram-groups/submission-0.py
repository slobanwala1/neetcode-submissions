from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # the charCount to list of anagrams
        # print(res)
        # newList = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        for s in strs:
            count = [0] * 26 # lowercase alphabets a -> z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) 
            # res is dictionary so the match of int array will be unique
            # Making it a tuple allows us to append the string to that specific list.
            # this way we can just return its values

        return list(res.values())  


