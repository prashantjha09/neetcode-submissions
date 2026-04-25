from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = defaultdict(int)
        for i in nums:
            frequency_count[i]=frequency_count[i]+1
        return sorted(frequency_count, key=lambda x: frequency_count[x])[-k:]



        