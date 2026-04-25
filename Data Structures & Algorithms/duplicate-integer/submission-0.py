from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_frequency = defaultdict(int)
        for i in nums:
            if num_frequency[i]>0:
                return True
            else:
                num_frequency[i] = num_frequency[i]+1
        return False
        